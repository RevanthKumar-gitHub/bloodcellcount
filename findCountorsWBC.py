import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt


def findNoWbcs(image):
    # load the imagecv2.imread
    image_normal = cv2.imread(image)
    # image_normal = cv2.blur(image_normal,(10,10))

    # find all the 'black' shapes in the image
    lower = np.array([0, 0, 0])
    upper = np.array([150, 150, 150])
    shapeMask = cv2.inRange(image_normal, lower, upper)
    # find the contours in the mask
    cnts, _ = cv2.findContours(
        shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # print ("# of Possible WBCs %d" % (len(cnts)))
    # cv2.imshow("Mask", shapeMask)

    # loop over the contours
    for c in cnts:
        # draw the contour and show it
        cv2.drawContours(image_normal, [c], -1, (0, 250, 0), 2)

    save_path = "./static/images/countWBC.jpg"
    path = "/images/countWBC.jpg"
    cv2.imwrite(save_path, image_normal)
    count = len(cnts)
    return path, count
