from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    # Class attributes, could be inherited
    id = db.Column(db.Integer, primary_key=True, unique=True)  # primary fro keys are required by SQLAlchemy

    role = db.Column(db.Integer, default=0)
    grad_year = db.Column(db.Integer, default=-1)

    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, email, name, password, role, grad_year):
        self.email = email
        self.password = password
        self.name = name

        self.role = role
        self.grad_year = grad_year

    def is_active(self):
        """True, as all users are active."""
        return True

    # IF YOU ENCOUNTERED SOME ERRORS, READ THE DOCUMENT FIRST ! YOU MAY FIND THINGS USEFUL!
    def get_id(self):
        """Return the id to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
