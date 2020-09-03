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
    return render_template("pages/index.html", title="Home")


@app.route('/blog')
def blog():
    return render_template("pages/blog.html",
                           posts=mongo.db.posts.find(), title="Blog")


@app.route('/about')
def about():
    return render_template("pages/about.html", title="About")


@app.route('/contact')
def contact():
    return render_template("pages/contact.html", title="Contact")


@app.route('/addpost')
def addpost():
    return render_template("pages/addpost.html", title="Add New Post")


@app.route('/viewpost/<post_id>')
def viewpost(post_id):
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("pages/viewpost.html", post=post)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEVELOPMENT'))
