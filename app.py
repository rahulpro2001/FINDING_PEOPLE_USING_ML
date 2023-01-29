from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        image = request.files["image"]
        image.save(secure_filename('uploaded_pic.png'))
        return redirect("/upload")
    return render_template("upload.html")

@app.route("/upload-existing", methods=["GET", "POST"])
def upload_existing():
    if request.method == "POST":
        image = request.files["image"]
        image.save(secure_filename('uploaded_pic.png'))
        return redirect("/upload-existing")
    return render_template("upload_existing.html")

@app.route("/view-person", methods=["GET", "POST"])
def view_person():
    if request.method == "POST":
        id = request.form["id"]
        img_names = os.listdir(os.path.join('static/train_data',id))
        images = []
        for img in img_names:
            images.append('static/train_data/'+id+'/'+img)
        print(images)
        # retrieve images of the person from server or database
        # images = get_images(name)
        # images = id
        print(id)

        return render_template("view-person.html", id=id, images=images)
    return render_template("view-person.html")

@app.route("/view-all", methods=["GET", "POST"])
def view_all():
    # retrieve all images from server or database
    images = "images"
    return render_template("view-all.html", images=images)


if __name__ == '__main__':
   app.run(debug = True)