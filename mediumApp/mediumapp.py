from flask import Flask, render_template, redirect, flash, url_for
from forms import Register, Login
from flask_sqlalchemy import SQLAlchemy

app = Flask("__name__")
app.config["SECRET_KEY"] = "9e881d1a94b2125d8df30ab584403075"
db = SQLAlchemy(app)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",posts=posts)

@app.route("/info")
def info():
    return render_template("info.html",title="ABOUT")

@app.route("/login")
def login():
    return render_template("login.html",title="LOG IN")

@app.route("/register")
def register():
    return render_template("register.html",title="REGISTER")