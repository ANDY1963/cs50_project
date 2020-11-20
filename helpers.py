#
import requests 
from flask import jsonify

def lookup():
    """Look up quote for symbol."""
    # Contact API
    response = requests.get(f"https://re.jrc.ec.europa.eu/api/MRcalc?lat={lat}&lon={lon}&outputformat=json&browser=1&horirrad=1")
    print(response)
    data=response.json()
    print(data)

lat = 52
lon = -3
lookup()