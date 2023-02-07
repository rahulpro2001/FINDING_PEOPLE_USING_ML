from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import json
#changes for json
import os

ALLOWED_EXTENSIONS = {'jpg'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    details = open("id_to_details.json", "r").read()
    details_into_json = json.loads(details)
    print(details_into_json)
    current_entries = len(details_into_json)
    id = str(current_entries + 1)
    if request.method == "POST":
        image = request.files["image"]
        details = open("id_to_details.json", "r").read()
        details_into_json = json.loads(details)
        current_entries = len(details_into_json)
        id = str(current_entries + 1)
        name = request.form['name']
        image = request.files['image']
        age = request.form['age']
        phone = request.form['phone']
        description = request.form['description']
        
        
        if not os.path.exists(f"static/train_data/{id}/"):
            os.makedirs(f"static/train_data/{id}/")

        data = {
            "id": id,
            "name": name,
            "photo": f"static/train_data/{id}/{id}_{len(os.listdir('static/train_data/'+id))}.jpg",
            "age": age,
            "where_found": "",
            "description": description,
            "contact": phone
        }

        details_into_json[id] = data
        with open("id_to_details.json", "w") as outfile:
            outfile.write(json.dumps(details_into_json))
        image.save((os.path.join(f"static/train_data/{id}/",f"{id}_{len(os.listdir('static/train_data/'+id))+1}.jpg")))
        
        return redirect("/upload")
    return render_template("upload.html",id=id)

@app.route("/upload-existing", methods=["GET", "POST"])
def upload_existing():
    if request.method == "POST":
        image = request.files["image"]
        image.save(secure_filename('uploaded_pic.png'))
        return redirect("/upload-existing")
    return render_template("upload_existing.html")

# @app.route("/view-person", methods=["GET", "POST"])
# def view_person():
#     if request.method == "POST":
#         id = request.form["id"]
#         img_names = os.listdir(os.path.join('static/train_data',id))
#         images = []
#         for img in img_names:
#             images.append('/static/train_data/'+id+'/'+img)
#         # retrieve images of the person from server or database
#         # images = get_images(name)
#         # images = id
#         print(id)
#         details = open("id_to_details.json", "r").read()
#         details_into_json = json.loads(details)
#         return render_template("view-person.html", id=id, images=images,name=details_into_json[id]["name"])
#     return render_template("view-person.html")

@app.route("/view-all", methods=["GET", "POST"])
def view_all():
    # retrieve all images from server or database
    
    # images = os.listdir('static/train_data')
    # return render_template("view-all.html", images=images)
    details = open("id_to_details.json", "r").read()
    details_into_json = json.loads(details)
    return render_template("view-all.html", detail = details_into_json)

@app.route("/view-profile/<id>", methods=["GET", "POST"])
def view_profile(id):
    img_names = os.listdir(os.path.join('static/train_data',id))
    images = []
    for img in img_names:
        images.append('/static/train_data/'+id+'/'+img)
    # retrieve images of the person from server or database
    # images = get_images(name)
    # images = id
    print(id)
    details = open("id_to_details.json", "r").read()
    details_into_json = json.loads(details)
    return render_template("view-profile.html", id=id, images=images,name=details_into_json[id]["name"],age=details_into_json[id]["age"],contact=details_into_json[id]["contact"],description=details_into_json[id]["description"])



if __name__ == '__main__':
   app.run(debug = True)