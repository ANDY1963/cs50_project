from helpers import contact_API
from flask import Flask, flash, jsonify, redirect, render_template, request, session
#from flask_session import Session
from flask import Flask
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def peak_sun():
    """Generate chart and table"""
     # if GET just show input form 
    if request.method == "GET":
        return render_template("index.html")

    # if POST get user input from form
    if request.method == "POST":
        print("doooooo")
        # get latitude from form
        lat=request.form.get("latitude")
        if not request.form.get("latitude"):
            return "must provide latitude"

        # get longitude from form
        lon=request.form.get("longitude")
        if not request.form.get("longitude"):
            return "must provide longitude"
        else:
            return "hello"

        