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
        return render_template("index.html", title = "home")

    # if POST get user input from form
    if request.method == "POST":
        # get latitude from form
        lat=request.form.get("latitude")
        if not request.form.get("latitude"):
            return "must provide latitude"

        # get longitude from form
        lon=request.form.get("longitude")
        if not request.form.get("longitude"):
            return "must provide longitude"
        # Call helper function from helpers.py; return value is a tuple of two lists
        data = contact_API(lat, lon)
        
        return render_template("chart.html", title = "chart", irrad_data = data[0], month_data = data[1], lat=lat, lon=lon)

        