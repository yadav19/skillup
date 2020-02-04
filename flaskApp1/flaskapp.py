from flask import Flask, redirect, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
app = Flask("__name__")

app.config['SECRET_KEY']="ed7ba13c56b036491babcdebc690e8f9"

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



@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='About')


@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@admin.com" and form.password.data == "asdasdasd":
            flash("You have been logged in!!!","success")
            return redirect(url_for('home'))
    return render_template('login.html',title="login",form=form)


@app.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}".format(form.username.data),"success")
        return redirect(url_for("home"))
    return render_template('register.html',title="Registration",form=form)

##conditional
if __name__ =="__main__":
    app.run(debug=True)