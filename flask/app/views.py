from app import app
from app import db 
from app.models import Users


@app.route("/")
def index():
    return "***Hello from Flask <3"
    

@app.route("/users/<username>", methods=["GET", "POST"])
def add_user(username):
    password = "test"
    add_user = Users(username, password)
    db.session.add(add_user)
    db.session.commit()

    return username