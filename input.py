import cv2
import numpy as np
from matplotlib import pyplot as plt
from randomFileNameGen import generate_random_filename

def input_image(image_path) : 
    image_normal= cv2.imread(image_path, 1)
    random_image_filename = generate_random_filename("jpg")
    save_path = "./static/images/"+random_image_filename
    path = "/images/"+random_image_filename
    cv2.imwrite(save_path, image_normal)
    return path
