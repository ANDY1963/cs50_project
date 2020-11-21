# Helper functions for Sunshine Hours App
#########################################
import requests 
def contact_API(lat, lon):
    """Get data from PVGIS API."""
    # Contact API. Python requests library method returns a response object. json method gets data from the object
    response = requests.get(f"https://re.jrc.ec.europa.eu/api/MRcalc?lat={lat}&lon={lon}&outputformat=json&browser=1&horirrad=1")
    return response.json()

lat = 51
lon = -3
data = contact_API(lat, lon)

print(data)


