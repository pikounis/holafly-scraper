# Import the json module
import json

# Path to the JSON file (replace this with the actual path where your file is stored)
file_path = 'countries_links.json'

# Load the JSON data from the file
with open(file_path, 'r') as file:
    countries_data = json.load(file)

# Count the number of countries by calculating the length of the list
number_of_countries = len(countries_data)

print(number_of_countries)
