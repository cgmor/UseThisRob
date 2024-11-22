# app/proximity_helper.py

import os
from app import supabase
from app.twilio_handler import send_text 
import requests
from math import radians, sin, cos, sqrt, atan2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

POSITIONSTACK_API_KEY = os.getenv("POSITIONSTACK_API_KEY")

def format_address(address_dict):
    """
    Format the address from the nested address dictionary.
    """
    if "address" in address_dict:
        address = address_dict["address"]
        city = address.get("city", "")
        state = address.get("state", "")
        street = address.get("street", "")
        zip_code = address.get("zip", "")
        # Combine components into a single address string
        return f"{street}, {city}, {state} {zip_code}"
    return None

def get_coordinates(address_dict):
    """
    Get the latitude and longitude of an address using Positionstack API.
    """
    address = format_address(address_dict)
    if not address:
        print("Address format is invalid.")
        return None

    print(f"Formatted address: {address}")

    # Positionstack API URL
    url = "http://api.positionstack.com/v1/forward"
    params = {
        "access_key": POSITIONSTACK_API_KEY,
        "query": address,
        "limit": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and data["data"]:
            location = data["data"][0]
            print(f"Coordinates for {address}: ({location['latitude']}, {location['longitude']})")
            return location["latitude"], location["longitude"]
        else:
            print("No results found for the address:", address)
            return None
    else:
        print("Error with Positionstack API:", response.status_code)
        return None


def calculate_distance(coord1, coord2):
    """
    Calculate the distance in kilometers between two coordinate pairs using the Haversine formula.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# Placeholder function for Google Maps API proximity check
def is_close(address1, address2, threshold_km=1.0):
    """
    Returns True if the distance between address1 and address2 is less than threshold_km (1 km by default).
    """
    coord1 = get_coordinates(address1)
    coord2 = get_coordinates(address2)

    # Debugging output
    print(f"Coordinates for address1: {coord1}")
    print(f"Coordinates for address2: {coord2}")

    # Ensure that both coordinates were successfully retrieved
    if coord1 is None or coord2 is None:
        print("Could not retrieve coordinates for one or both addresses.")
        return False

    # Calculate the distance
    distance = calculate_distance(coord1, coord2)
    print(f"Distance between addresses: {distance} km")
    return distance < threshold_km

def check_proximity_and_notify(target_address):
    print("Called CheckProx")
    """
    Checks the database for addresses close to the given target_address.
    If a close match is found, sends a notification via Twilio.
    """
    # Step 1: Fetch all addresses and numbers from the database
    response = supabase.table("CustomerInfo").select("address, Phone1").execute()
    
    if not hasattr(response, "data") or response.data is None:
        print("Error fetching addresses from database.")
        return

    # Step 2: Loop through the addresses in the database
    for entry in response.data:
        db_address = entry.get("address")
        phone1 = entry.get("Phone1")
        print(get_coordinates(db_address))
        
        # Step 3: Check if the current db_address is close to the target_address
        if is_close(db_address, target_address):
            # If close, send a text notification
            print("A nearby address was found")
            message = f"A nearby address was found: {db_address}"
            print(f"Phone1: {phone1}")
            send_text(message)
            print("Notification sent.")
            return  # Exit after the first match, or continue if multiple notifications are needed

    print("No close addresses found.")