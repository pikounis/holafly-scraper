import json

file_path = 'countries_links.json'  # Update this path
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Use a set to track seen countries
seen_countries = set()

# Initialize a list to hold unique entries
unique_entries = []

# Iterate over each entry in the JSON data
for entry in json_data:
    country = entry['country']

    # Check if the country is already in the set
    if country not in seen_countries:
        seen_countries.add(country)
        unique_entries.append(entry)  # Add unique entry to the list

# The unique_entries list now contains only one entry per country

# Optionally, you can overwrite the original JSON file with unique entries
with open(file_path, 'w') as file:
    json.dump(unique_entries, file, indent=4)

print("Duplicates removed, keeping only one entry per country.")
