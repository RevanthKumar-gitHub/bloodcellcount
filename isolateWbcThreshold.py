import cv2
import numpy as np
from matplotlib import pyplot as plt

def wbcThresholding(im_gray):
    img = cv2.medianBlur(im_gray, 5)#medianBlur
    ret, th1 = cv2.threshold(img, 120, 50, cv2.THRESH_BINARY)#thresholdvalue=120
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    titles = [
    "Original Image",
    "Global Thresholding (v = 127)",
    "Adaptive Mean Thresholding",
    "Adaptive Gaussian Thresholding",
    ]
    images = [img, th1, th2, th3]
    
    paths=[]
    for i in range(4):
        save_path = "./static/images/"+titles[i]+".jpg"
        path = "/images/"+titles[i]+".jpg"
        paths.append(path)
        cv2.imwrite(save_path, images[i])
        
    return paths