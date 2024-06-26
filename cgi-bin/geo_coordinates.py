#!/usr/bin/env python3

import cgi
import cgitb
import json
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers including CORS headers
print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")  # Allow all origins
print()  # Blank line required between headers and body

# Parse the query parameters
form = cgi.FieldStorage()
location_name = form.getvalue("location")

def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    try:
        location = geolocator.geocode(location_name, timeout=10)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude}
        else:
            return {"error": "Location not found"}
    except GeocoderTimedOut:
        return {"error": "Geocoding service timed out"}
    except GeocoderServiceError as e:
        return {"error": f"Geocoding service error: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

if location_name:
    # Get coordinates for the provided location
    coordinates = get_coordinates(location_name)
else:
    coordinates = {"error": "No location provided"}

# Output the result as JSON
print(json.dumps(coordinates))