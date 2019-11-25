from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id =db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255), unique = True, index = True)
    bio=db.Column(db.String(255))
    avatar=db.Column(db.String())
    posts=db.Column()

    password=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, passwprd):
        return check_password_hash(password)


    def __repr__(self):
        return f'User {self.username}'

class Post:

    __tablename__='posts'
        id=db.Column(db.Integer, primary_key=True)
        category=db.Column(db.String())
        title=db.Column
