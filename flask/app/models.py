from app import db


class Users(db.Model):
    __tablename__  = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(500))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Username: {self.username}"