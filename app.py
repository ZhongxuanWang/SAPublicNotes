from flask import Flask, request, flash, render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy

# import requests as req
app = Flask(__name__)

db = SQLAlchemy()


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return render_template('main.html')
    else:
        return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    """A Search System for notes"""

    return render_template('under_dev.html')


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    return render_template('under_dev.html')


# def create_app():
#     app.config['SECRET_KEY'] = 'wwzzxxsecretekeytodatabase'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'
#
#     db.init_app(app)
#
#     # blueprint for auth routes in our app
#     from auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)
#
#     app_blueprint = Blueprint('app', __name__)
#     app.register_blueprint(app_blueprint)
#     return app


def run_app():
    app.config['SECRET_KEY'] = 'wwzzxxsecretekeytodatabase'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'

    db.init_app(app)

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # app_blueprint = Blueprint('app', __name__)
    # app.register_blueprint(app_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        print('in load user function')
        # print('User ID:', user_id)
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from user import User
        return User.query.get(int(user_id))
    app.run(debug=True)


if __name__ == 'main':
    # print('hello')
    run_app()
