from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from blog import db
from . import bp
from .auth_forms import (
    LoginForm,
    SignupForm,
    ResetPasswordRequestForm,
    ResetPasswordForm,
)
from blog.models import User
from .auth_email import send_password_reset_email


@bp.route("/login", methods=["GET", "POST"])
def login():
    """
    User login page.

    GET: Serve Log-in page.
    POST: If form is valid and new user creation succeeds, redirect user to the logged-in homepage.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template("auth/login.html", title="Sign In", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    """
    User sign-up page.

    GET: Serve sign-up page.
    POST: If submitted credentials are valid, redirect user to the logged-in homepage.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("auth.login"))
    return render_template("auth/signup.html", title="Sign up", form=form)


@bp.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    """ reset password request route """
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash("Check your email for the instructions to reset your password")
        return redirect(url_for("auth.login"))
    return render_template(
        "auth/reset_password_request.html", title="Reset Password", form=form
    )


@bp.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    """ reset password route"""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("main.index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Your password has been reset.")
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html", form=form)
