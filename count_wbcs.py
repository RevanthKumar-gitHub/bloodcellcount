from input import input_image
from kMeansSegmentation import kMeans_seg
from gray_scale import grayScale
from isolateWbcThreshold import wbcThresholding
from originalImageThresh import originalImageTresh
from houghsGradientWbc import houghsGradient
from findCountorsWBC import findNoWbcs
from thresholdingRBC import thresholdRBC
from subratWBC import subtractWBC
from kmeansRbc import kmeansClusteringRBC
from count_rbcs import countRBC
from predict import predict_image

def count_wbcs(image_path):
    image_normal_path = input_image(image_path)
    kmeans_input_path = "./static" + image_normal_path
    prediction = predict_image(kmeans_input_path)
    uploadedImageValid=0
    if prediction == 1:
        uploadedImageValid  = 1
    else : 
        uploadedImageValid = 0
    kmeans_seg_path, kMeans_seg_img = kMeans_seg(kmeans_input_path)
    image_gray_path, gray_image = grayScale(kMeans_seg_img)
    paths = wbcThresholding(gray_image)
    normal_paths, th1 = originalImageTresh(kmeans_input_path)
    houghsCount = 0
    count = houghsGradient(th1)
    if count == 0:
        houghsCount = 0
    else:
        houghsCount = count

    wbcCountPath, wbcCount = findNoWbcs("./th1.jpg")
    
    #count rbcs
    
    rbcPaths = thresholdRBC(gray_image)
    subtractWBC() #subtracting wbc to count rbc
    kmeansClusteringRBC()
    countrbc,countRbc = countRBC()
    
    return (
        image_normal_path,
        kmeans_seg_path,
        image_gray_path,
        paths,
        normal_paths,
        houghsCount,
        wbcCountPath,
        wbcCount,
        rbcPaths,
        countrbc,
        countRbc,
        uploadedImageValid
    )
    
