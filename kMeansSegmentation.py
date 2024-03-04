import numpy as np
import cv2
from matplotlib import pyplot as plt
from randomFileNameGen import generate_random_filename

def kMeans_seg(image_path) : 

    img = cv2.imread(image_path)
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 3
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    
    random_image_filename = generate_random_filename("jpg")
    save_path = "./static/images/"+random_image_filename
    path = "/images/"+random_image_filename
    cv2.imwrite(save_path, res2)
    return path,res2