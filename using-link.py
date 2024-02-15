import requests
from bs4 import BeautifulSoup
import json

# The URL from where to fetch the HTML content
url = 'https://esim.holafly.com/shop/?first_letter=C&last_letter=E'

# Use requests to fetch the content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags with class 'nav-link'
anchors = soup.find_all('a', class_='nav-link')

# Extract the countries and links
countries_links = [{'country': anchor.text.strip(), 'link': anchor['href']} for anchor in anchors]

# Convert the list to JSON format
json_data = json.dumps(countries_links, indent=4)

# Define the JSON file name
file_name = 'countries_links.json'

# Save the JSON data to the file
with open(file_name, 'w') as file:
    file.write(json_data)

print(f'JSON data has been saved to {file_name}')
