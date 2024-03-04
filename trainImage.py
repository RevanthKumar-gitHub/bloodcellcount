import os
import cv2
import numpy as np
from skimage import feature
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def extract_hog_features(images):
    features = []
    for img in images:
        hog_feature = feature.hog(img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), transform_sqrt=True, block_norm="L2-Hys")
        features.append(hog_feature)
    return np.array(features)

# Specify the desired width
desired_width = 300  # Adjust as needed
# Read the image
img = cv2.imread("./bccDataset/not_blood_smear/ATVB_email_attachment_SMC_1482420395_1.jpg", cv2.IMREAD_GRAYSCALE)
# Calculate the aspect ratio
aspect_ratio = img.shape[1] / img.shape[0]
# Calculate the corresponding height
desired_height = int(desired_width / aspect_ratio)


# Load blood smear images
blood_smear_images = load_images_from_folder('./bccDataset/blood_smear')
blood_smear_labels = np.ones(len(blood_smear_images))

# Load non-blood smear images
not_blood_smear_images = load_images_from_folder('./bccDataset/not_blood_smear')
not_blood_smear_labels = np.zeros(len(not_blood_smear_images))

# Ensure all images have the same dimensions
blood_smear_images = [cv2.resize(img, (desired_width, desired_height)) for img in blood_smear_images]
not_blood_smear_images = [cv2.resize(img, (desired_width, desired_height)) for img in not_blood_smear_images]

# Combine the datasets
images = np.concatenate([blood_smear_images, not_blood_smear_images])
labels = np.concatenate([blood_smear_labels, not_blood_smear_labels])

# Extract HOG features
features = extract_hog_features(images)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=8)

# Train an SVM classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)

# Save the trained model
joblib.dump(svm_classifier, 'blood_smear_classifier.pkl')

# Evaluate the model on the test set
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on the test set: {accuracy * 100:.2f}%")
