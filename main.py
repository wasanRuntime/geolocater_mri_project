from geopy.geocoders import Nominatim
import pandas as pd
import re

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

# Define a list of locations
locations = ['Central Bank of Kenya', 'Nairobi National Park', 'Giraffe Centre', 'Mombasa Road', 'Uhuru Park', 'Thika Road Mall']

# Create an empty list to store location data
location_data = []

# Loop through the locations and get the latitude and longitude data
for location in locations:
    location_info = geolocator.geocode(location)
    if location_info is not None:  # Check if the location is valid
        latitude = location_info.latitude
        longitude = location_info.longitude
        address = location_info.address
        road = re.search(r"\broad\b", address, re.IGNORECASE)
        road_name = road.group(0) if road else ''
        data = {'Location': location, 'Address': address, 'Latitude': latitude, 'Longitude': longitude}
        location_data.append(data)

# Create a Pandas DataFrame with the location data
df = pd.DataFrame(location_data)

# Save the data to an Excel file
filename = 'location_data12.xlsx'
df.to_excel(filename, index=False)
