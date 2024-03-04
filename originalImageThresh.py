import cv2
import numpy as np


def originalImageTresh(image_path):
    image_normal = cv2.imread(image_path, 1)

    image_normal = cv2.cvtColor(image_normal, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(image_normal, 5)

    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
    th3 = cv2.adaptiveThreshold(
        img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    titles = [
        "Normal Image",
        "Global Thresholding Normal(v = 127)",
        "Adaptive Mean Thresholding Normal",
        "Adaptive Gaussian Thresholding Normal",
    ]
    images = [img, th1, th2, th3]
    paths = []
    for i in range(4):
        save_path = "./static/images/" + titles[i] + ".jpg"
        path = "/images/" + titles[i] + ".jpg"
        paths.append(path)
        cv2.imwrite(save_path, images[i])
    cv2.imwrite("th1.jpg", th1)
    cv2.imwrite("img.jpg", img)
    return paths,th1

