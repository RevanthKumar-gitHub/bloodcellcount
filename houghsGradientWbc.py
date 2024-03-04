import cv2
import numpy as np

def houghsGradient(th1):
    # Assuming 'th1' is your input image
    cimg = th1

    # Convert to grayscale if needed
    # cimg = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)  # Remove this line

    # Apply median blur if needed
    cimg = cv2.medianBlur(cimg, 5)

    # Detect circles using HoughCircles
    circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, dp=1, minDist=3, param1=5, param2=3, minRadius=2, maxRadius=30)

    # Check if circles were found
    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

        return circles.shape[1]
    else:
        return 0  


