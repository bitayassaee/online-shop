from flask import Blueprint

app = Blueprint("general",__name__)

@app.route('/')
def main():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "about usg"