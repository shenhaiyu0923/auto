import time

from functools import wraps
from Public.BasePage import BasePage
from Public.ReportPath import ReportPath
from Public.Log import Log
import os
import imageio
import shutil

flag = 'IMAGE:'
log = Log()


def _screenshot(name):
    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screenshot = name + '-' + date_time + '.PNG'
    # path = ReportPath().get_path() + '/' + screenshot
    path = os.path.join(ReportPath().get_path(), screenshot)
    driver = BasePage().get_driver()
    driver.screenshot(path)
    return screenshot


def _screenshot_for_gif(step_name):
    tmp_path = os.path.join(ReportPath().get_path(), 'tmp')
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    # tmpshot = tmp + str(round(time.time() * 1000)) + '.PNG'
    tmpshot = str(round(time.time() * 1000)) + '_' + step_name + '.PNG'
    path = os.path.join(tmp_path, tmpshot)
    driver = BasePage().get_driver()
    driver.screenshot(path)
    return path


def _create_gif(step_name):
    '''
    生成gif文件，原始图片仅支持png格式
    gif_name ： 字符串，所生成的 gif 文件名，带 .gif 后缀
    path :      需要合成为 gif 的图片所在路径
    duration :  gif 图像时间间隔
    '''

    frames = []
    path = os.path.join(ReportPath().get_path(), 'tmp')
    if not os.path.exists(path):
        pass
    else:
        pngFiles = os.listdir(path)
        image_list = [os.path.join(path, f) for f in pngFiles]
        list.sort(image_list)
        for image_name in image_list:
            # 读取 png 图像文件
            frames.append(imageio.imread(image_name))
        # 保存为 gif
        # gif_name = str(round(time.time() * 1000)) + '_' + step_name + '.gif'
        gif_name = step_name + '.gif'
        gif_path = os.path.join(ReportPath().get_path(), gif_name)
        imageio.mimsave(gif_path, frames, 'GIF', duration=0.8)
        # shutil.rmtree(path)
        os.rename(path, os.path.join(ReportPath().get_path(), step_name))
        return gif_name


def teststep(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('--> %s' % func.__qualname__)
            ret = func(*args, **kwargs)
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'AssertionError', 'Error')
            raise AssertionError(e)
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'Exception', 'Error')
            raise Exception(e)
        finally:
            _screenshot_for_gif(func.__qualname__)   # 截取gif生成用图

    return wrapper


def teststeps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('--> %s' % func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('  <-- %s, %s', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('  <-- %s, %s, %s', func.__qualname__, 'AssertionError', 'Error')
            raise AssertionError(e)
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('  <-- %s, %s, %s', func.__qualname__, 'Exception', 'Error')
            raise Exception(e)
        # finally:
        #     _screenshot_for_gif()  # 截取gif生成用图

    return wrapper


def testcase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.d('--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('<-- %s, %s\n', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')

            if flag in str(e):
                raise AssertionError(e)
            else:
                raise AssertionError(flag + _screenshot(func.__qualname__))
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')

            if flag in str(e):
                raise Exception(e)
            else:
                raise Exception(flag + _screenshot(func.__qualname__))
        finally:
            a = _create_gif(func.__doc__)
            if a:
                log.i(flag + a)  # 生成gif 并生成各case文件夹

    return wrapper


def _wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.d('--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('<-- %s, %s\n', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')

            if flag in str(e):
                raise AssertionError(e)
            else:
                raise AssertionError(flag + _screenshot(func.__qualname__))
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')

            if flag in str(e):
                raise Exception(e)
            else:
                raise Exception(flag + _screenshot(func.__qualname__))

    return wrapper


def setup(func):
    return _wrapper(func)


def teardown(func):
    return _wrapper(func)


def setupclass(func):
    return _wrapper(func)


def teardownclass(func):
    return _wrapper(func)
