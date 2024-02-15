import json


# Assuming the JSON data is loaded from 'countries_links.json'
file_path = 'results.json'  # Update this path

countries_with_empty_packages = []

# Load JSON data from a file
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Check which country has empty packages
for entry in json_data:
    if not entry["packages"]:  # Check if the 'packages' list is empty
        countries_with_empty_packages.append(entry["country"])

# Print countries with empty packages
print("Countries with empty packages:")
for country in countries_with_empty_packages:
    print(country)
