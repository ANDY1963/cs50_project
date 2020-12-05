##########################################
# Helper functions for Sunshine Hours App
##########################################

# Import python requests module (library) to deal with requests
import requests 
def contact_API(lat, lon):
    """Get data from PVGIS API."""
    # Contact API. Python requests library method returns a response object. 
    response = requests.get(f"https://re.jrc.ec.europa.eu/api/MRcalc?startyear=2016&endyear=2016&lat={lat}&lon={lon}&outputformat=json&browser=1&horirrad=1")
    # json method gets data from the object
    data = response.json()

    # Extract list of output dicts for each month
    output_list = data["outputs"]["monthly"]

    # Initialise python dicts for irradiance and month data
    irrad_data = []
    month_data = []

    # Loop output_list to extract 
    for item in output_list:
        irrad_data.append(item["H(h)_m"])
        month_data.append(item["month"])
        
    # Return tuple containing two lists
    return (irrad_data, month_data)





