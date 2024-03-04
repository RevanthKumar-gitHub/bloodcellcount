import PIL
import cv2

def diff(img,img1): # returns just the difference of the two images
    return cv2.subtract(img,img1)

def subtractWBC() : 
    th1= cv2.imread('th1.jpg')
    img= cv2.imread('img.jpg')
    sub_img= diff(th1,img)  
    cv2.imwrite('sub_img.jpg',sub_img)




