from flask import Flask, render_template, redirect, flash, url_for
from forms import Register, Login
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
app = Flask("__name__")
app.config["SECRET_KEY"] = "9e881d1a94b2125d8df30ab584403075"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

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

class Users(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    profile_pic = db.Column(db.String(30), nullable=False, default="default.jpg")
    posts = db.relationship("Posts", backref="author",lazy=True) # 1. which model does it relate to //2. what will be reference name of it the other model //3. True means load the data necessary in one go

    def __repr__(self):
        return "User({}, {}, {}, {})".format(self.uid,self.username,self.email,self.profile_pic)

class Posts(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    title = db.Column(db.String(40), nullable=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.uid"), nullable=False) # u in users is small as sqlite saves the tables in small letters
    def __repr__(self):
        return "Post({}, {}, {})".format(self.pid, self.post_date, self.title)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",posts=posts)

@app.route("/info")
def info():
    return render_template("info.html",title="ABOUT")

@app.route("/login",methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        flash(" you have succesfully logged in {}".format(form.email.data),"success")
        return redirect(url_for('index'))
    return render_template("login.html",title="LOG IN",form=form)

@app.route("/register",methods=["GET", "POST"])
def register():
    form = Register()
    if form.validate_on_submit():

        flash(" you have successfully registered {}".format(form.username.data),"success")
        return redirect(url_for('index'))
    return render_template("register.html",title="REGISTRATION",form = form)