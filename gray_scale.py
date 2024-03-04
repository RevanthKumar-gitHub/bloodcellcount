import cv2
from randomFileNameGen import generate_random_filename

def grayScale(kmeans_seg_img) :
    im_gray=cv2.cvtColor(kmeans_seg_img,cv2.COLOR_BGR2GRAY)
    random_image_filename = generate_random_filename("jpg")
    save_path = "./static/images/"+random_image_filename
    path = "/images/"+random_image_filename
    cv2.imwrite(save_path, im_gray)
    return path,im_gray  