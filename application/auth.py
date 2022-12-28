from algosdk import mnemonic
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user
from application.algod import create_account
from application.forms import *
from .models import User
from .query import isLoginValid, username_exist, create_user

login_manager = LoginManager()

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Default login page"""
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))

    form = LoginForm()
    if form.validate_on_submit():

        try:
            print(isLoginValid(phone_number=form.phone.data, pin=form.pin_number.data))
            if isLoginValid(phone_number=form.phone.data, pin=form.pin_number.data):
                print("Successful")
                user = User(phone=form.phone.data)
                login_user(user)
                return redirect(url_for('main_bp.index'))
            else:
                return render_template('login.html', messages="error", form=form)
        except Exception as err:
            print(err)
            flash(err)
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))

    form = SignUpForm()

    if form.validate_on_submit():
        name = form.full_name.data
        phone_no = form.phone.data
        email = form.email.data
        pin = form.pin_number.data
        pin_confirm  = form.pin_number_confirmation.data
        try:
            if pin == pin_confirm:
                if not username_exist(phone_no):
                    create_user(full_name=name, phone=phone_no,pin=pin,email_address=email)
                    user = User(phone=phone_no)
                    login_user(user)
                    return redirect(url_for('main_bp.index'))
                else:
                    flash("Phone number is already registered")
                    render_template('signup.html', form=form)

            else:
                flash("Pin numbers doesn't match")
                render_template('signup.html', form=form)


        except Exception as err:
            flash(err)
            return render_template('signup.html', form=form)

    return render_template('signup.html', form=form)




@login_manager.user_loader
def load_user(user_id):
    """User load logic"""
    return User(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to login page"""
    return redirect(url_for('auth_bp.login'))
