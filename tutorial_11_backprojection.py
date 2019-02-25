import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 360], [0, 180, 0, 256])  # 计算直方图
    # cv.imshow("hist2d_demo", hist)
    plt.imshow(hist, interpolation="nearest")  # 直方图显示
    plt.title("2D Histogram")
    plt.show()


# OpenCV 提供的函数 cv2.calcBackProject() 可以用来做直方图反向 投影。
# 它的参数与函数 cv2.calcHist 的参数基本相同。其中的一个参数是我 们要查找目标的直方图。
# 同样再使用目标的直方图做反向投影之前我们应该先对其做归一化处理。
# 返回的结果是一个概率图像
def back_projection_demo():
    sample = cv.imread("roi.png")
    target = cv.imread("CrystalLiu3.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow("sample", sample)
    cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
    # cv.NORM_MINMAX对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
    # 归一化后的图像便于显示，归一化后到0,255之间了
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)


src = cv.imread("CrystalLiu1.jpg")  # 读入图片放进src中
cv.namedWindow("Crystal Liu")  # 创建窗口
cv.imshow("Crystal Liu", src)  # 将src图片放入该创建的窗口中
# hist2d_demo(src)
back_projection_demo()

cv.waitKey(0) # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口
cv.destroyAllWindows()  # 关闭所有窗口