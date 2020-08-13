import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("pages/index.html")


@app.route('/blog')
def blog():
    return render_template("pages/blog.html", posts=mongo.db.posts.find())


@app.route('/about')
def about():
    return render_template("pages/about.html")


@app.route('/contact')
def contact():
    return render_template("pages/contact.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEVELOPMENT'))
