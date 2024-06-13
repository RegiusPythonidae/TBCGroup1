from flask import render_template, redirect
from flask_login import login_user, logout_user, current_user, login_required

from forms import RegisterForm, LoginForm
from models import Product, User
from ext import app, db

@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products, role="Guest")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")

@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product)


@app.route("/add_product")
@login_required
def add_product():
    return render_template("add_product.html")