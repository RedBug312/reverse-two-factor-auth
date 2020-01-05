from flask import Blueprint, request, render_template, redirect, url_for, make_response, g, flash, current_app

from ..models import auth


signin = Blueprint('signin', __name__)


@signin.route('/signin')
def index():
    brokers = current_app.config['BROKERS']
    recaptcha = current_app.config['RECAPTCHA_SITEKEY']
    return render_template('signin.pug', title='Login', code='123456',
                           brokers=brokers, recaptcha=recaptcha)


@signin.route('/signin/redirect', methods=['POST'])
def result():
    username = request.form.get('username')
    password = request.form.get('password')
    badges = request.form.get('badges')
    if username is None or password is None:
        flash('You\'ve forgotten the username or password.', 'error')
        return redirect(url_for('signin.index'))
    if not auth.verify_password_callback(username, password, badges):
        flash('You\'ve given mismatched password or badges.', 'error')
        return redirect(url_for('signin.index'))
    res = make_response(redirect(url_for('index')))
    res.set_cookie('token', g.user.generate_auth_token())
    return res
