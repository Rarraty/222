from flask_bootstrap import Bootstrap
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.debug = True


@app.route('/')
def index():
    return render_template("Warning.html")


@app.route('/index.html')
def about():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
