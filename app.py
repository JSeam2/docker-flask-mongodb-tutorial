import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient


app = Flask("DockerTutorial")

# To change accordingly 
# print(os.environ)
client = MongoClient(os.environ["DB_PORT_27017_TCP_ADDR"], 27017)
db = client.appdb

@app.route("/")
def index():
    _items = db.appdb.find()
    items = [items for items in _items]

    return render_template("index.html", items=items)


@app.route("/new", methods=["POST"])
def new():
    data = {
        "helloworld": request.form["helloworld"]
    }

    db.appdb.insert_one(data)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

