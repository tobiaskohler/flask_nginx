from app import app

@app.route("/")
def index():
    return "***Hello 1from Flask <3"