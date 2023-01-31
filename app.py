from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import json
#changes for json
import os



#-------------------
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
        # retrieve images of the person from server or database
        # images = get_images(name)
        # images = id
        print(id)
        details = open("id_to_details.json", "r").read()
        details_into_json = json.loads(details)
        return render_template("view-person.html", id=id, images=images,name=details_into_json[id]["name"])
    return render_template("view-person.html")

@app.route("/view-all", methods=["GET", "POST"])
def view_all():
    # retrieve all images from server or database
    
    # images = os.listdir('static/train_data')
    # return render_template("view-all.html", images=images)
    details = open("id_to_details.json", "r").read()
    details_into_json = json.loads(details)
    return render_template("view-all.html", detail = details_into_json)


if __name__ == '__main__':
   app.run(debug = True)