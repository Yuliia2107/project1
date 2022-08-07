
from cs50 import SQL
from flask import Flask,redirect, render_template, request, session

# Configure application
app = Flask(__name__)

REGISTRANTS = {}

db = SQL("sqlite:///travelers.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name :
        return render_template("error.html", message="Try input name again")
    REGISTRANTS[name] = name

    return redirect("/start")


@app.route("/start",  methods=["GET", "POST"])
def start():
    if request.method == "POST":
            return redirect("/")

    return render_template("start.html")
