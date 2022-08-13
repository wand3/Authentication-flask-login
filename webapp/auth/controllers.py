from flask import render_template, redirect, request, url_for, flash, Blueprint
from .forms import RegisterForm, LoginForm
from ..models import User
from .. import db
from flask_login import login_user, login_required, logout_user

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        #set password to bcrypt hash
        user.set_password(password=form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful Login to continue')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User.query.filter_by(email=form.username_or_email.data).first()
    user1 = User.query.filter_by(username=form.username_or_email.data).first()

    if form.validate_on_submit():
        if user1 is not None and (user1.check_password(form.password.data)):
            #login user and remember_me cookie session
            if user1:
                login_user(user1, form.remember_me.data)

            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)

        elif user is not None and (user.check_password(form.password.data)):
            # login user and remember_me cookie session
            if user:
                login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)
        else:
            flash('Invalid username or password')

    return render_template('login.html', form=form, remember_me=True)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.home'))

