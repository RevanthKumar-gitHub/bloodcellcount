import cv2
from skimage import feature
import joblib

# Load the trained model
svm_classifier = joblib.load("blood_smear_classifier.pkl")


def predict_image(img_path):
    # Specify the desired width
    desired_width = 300  # Adjust as needed
    # Read the image
    img = cv2.imread("./bccDataset/not_blood_smear/ATVB_email_attachment_SMC_1482420395_1.jpg", cv2.IMREAD_GRAYSCALE)
    # Calculate the aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    # Calculate the corresponding height
    desired_height = int(desired_width / aspect_ratio)
    # Read the image in grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image if needed (adjust width and height as necessary)
    img = cv2.resize(img, (desired_width, desired_height))

    # Extract HOG features
    hog_feature = feature.hog(
        img,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        transform_sqrt=True,
        block_norm="L2-Hys",
    )
    
    # Make prediction
    prediction = svm_classifier.predict([hog_feature])
    return prediction[0]



# Example usage

