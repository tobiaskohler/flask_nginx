from app import app
from app import db 
from app.models import Users


@app.route("/")
def index():
    return "***Hello from Flask hello world <3"
    

@app.route("/post/users/<username>", methods=["GET", "POST"])
def add_user(username):
    password = "test"
    add_user = Users(username, password)
    db.session.add(add_user)
    db.session.commit()

    return username

@app.route("/get/users/<username>", methods=["GET", "POST"])
def get_user(username):
    get_user=Users.query.filter_by(username=username).first()

    if get_user is None:
        return f"{username} ####wurde N I C H T gefunden!"

    else:
        return f"{get_user.username} ####wurde gefunden"

    