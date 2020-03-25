from skimage.measure import compare_ssim
import imutils
import cv2
import os


def image_identify(standard_path, test_path, result_path):
    image1 = cv2.imread(standard_path)
    image2 = cv2.imread(test_path)

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 接下来，计算两个灰度图像之间的结构相似度指数
    (score, diff) = compare_ssim(gray1, gray2, full=True)
    print(score)
    if score != 1:
        diff = (diff * 255).astype("uint8")
        # 找到不同点的轮廓以致于我们可以在被标识为不同的区域周围放置矩形
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        # 找到一系列区域，在区域周围放置矩形
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image1, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
        # cv2.imshow("Modified", image2)
        cv2.imwrite(result_path, image2)
        # cv2.waitKey(0)


def get_files(path):
    all = []
    for fpathe, dirs, fs in os.walk(path):   # os.walk是获取所有的目录
        for f in fs:
            filename = os.path.join(fpathe, f)
            if filename.endswith('jpg') or filename.endswith('PNG'):  # 判断是否是"xxx"结尾
                all.append(filename)
    return all


def get_dir(path):
    all = []
    dirs = os.listdir(path)
    for file in dirs:
        report_path = os.path.join(path, file)
        if os.path.isdir(report_path):
            all.append(report_path)
    return all


if __name__ == '__main__':
    print(get_files(r"E:\vova_uitest\TestSuite_mainflow\Compare"))
    print(get_files(r"E:\vova_uitest\TestSuite_mainflow\TestReport\SM-G9500_988b1c45544845595a"))
    print(get_dir(r"E:\vova_uitest\TestSuite_mainflow\TestReport"))

