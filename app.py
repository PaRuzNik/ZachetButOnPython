from flask import Flask
from flask import render_template
from flask import request
from flask.json import jsonify


static_url_path = "/static/"

app = Flask(
    "my_app",
    static_url_path=static_url_path,
    static_folder="./img",
)

names = {
    0: "Евграф",
    1: "Понтиафей",
    2: "Даздраперма",
    3: "Люциус",
}

images = {
    0: "back2.jpg",
    1: "ONLZZq8mXRU.png",
    2: "phone.jpg",
    3: "test1.jpg",
}


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        return render_template("index.html")

    id = int(request.form.get('id'))
    context = {
        'name': names[id],
        'image': static_url_path + images[id]
    }
    return render_template("index.html", **context)


app.run()
