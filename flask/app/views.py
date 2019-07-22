from app import app

@app.route("/")
def index():
    return "***Hello 1from Flask <3"
    

@app.route("/users/<username>", methods=["GET", "POST"])
def add_user(username):
    password = "test"
    add_user = Users(username, password)
    db.session.add(add_user)
    db.session.commit()

    return username