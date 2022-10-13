from lab1 import app


@app.route("/")
def default_page():
    return "Default page"
