from flask import Flask, render_template, request
import os
from count_wbcs import count_wbcs
import glob

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

STATIC_IMAGES_FOLDER = "static/images"
app.config["STATIC_IMAGES_FOLDER"] = STATIC_IMAGES_FOLDER


def delete_existing_images():
    # Get a list of all image files in the static/images folder
    image_files = glob.glob(os.path.join(app.config["STATIC_IMAGES_FOLDER"], "*.*"))

    # Delete each image file
    for image_file in image_files:
        os.remove(image_file)

    image_files = glob.glob(os.path.join(app.config["UPLOAD_FOLDER"], "*.*"))

    # Delete each image file
    for image_file in image_files:
        os.remove(image_file)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", error="No file part")

        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", error="No selected file")

        if file:
            delete_existing_images()
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            if not os.path.exists(app.config["UPLOAD_FOLDER"]):
                os.makedirs(app.config["UPLOAD_FOLDER"])
            file.save(file_path)
            (
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
                uploadImageValid,
            ) = count_wbcs(file_path)
            return render_template(
                "index.html",
                image_normal_path=image_normal_path,
                kmeans_seg_path=kmeans_seg_path,
                image_gray_path=image_gray_path,
                global_thresholding=paths[1],
                adaptive_mean_thresholding=paths[2],
                adaptive_gausian_thresholding=paths[3],
                normal_threshold=normal_paths[0],
                normal_global=normal_paths[1],
                adaptive_mean=normal_paths[2],
                adaptive_gaussian=normal_paths[3],
                houghsCount=houghsCount,
                wbcCountPath=wbcCountPath,
                wbcCount=wbcCount,
                rbc_global_thresholding=rbcPaths[1],
                rbc_adaptive_mean_thresholding=rbcPaths[2],
                rbc_adaptive_gausian_thresholding=rbcPaths[3],
                countRbcPath = countrbc,
                countrbc = countRbc,
                uploadImageValid = uploadImageValid,
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
