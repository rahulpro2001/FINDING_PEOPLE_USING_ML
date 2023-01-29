from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
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


@app.route("/view-person", methods=["GET", "POST"])
def view_person():
    if request.method == "POST":
        name = request.form["name"]
        # retrieve images of the person from server or database
        images = get_images(name)
        return render_template("view-person.html", name=name, images=images)
    return render_template("view-person.html")

@app.route("/view-all")
def view_all():
    # retrieve all images from server or database
    images = get_all_images()
    return render_template("view-all.html", images=images)

		
if __name__ == '__main__':
   app.run(debug = True)