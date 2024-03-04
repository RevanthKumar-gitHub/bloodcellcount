import cv2
import numpy as np
from matplotlib import pyplot as plt


# isolating RBCs
def thresholdRBC(im_gray):
    img = cv2.medianBlur(im_gray, 5)

    ret, th1 = cv2.threshold(img, 125, 200, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
    th3 = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    titles = [
        "Original Image RBC",
        "Global Thresholding (v = 127) RBC",
        "Adaptive Mean Thresholding RBC",
        "Adaptive Gaussian Thresholding RBC",
    ]
    images = [img, th1, th2, th3]
    paths = []
    for i in range(4):
        save_path = "./static/images/" + titles[i] + ".jpg"
        path = "/images/" + titles[i] + ".jpg"
        paths.append(path)
        cv2.imwrite(save_path, images[i])
    return paths
