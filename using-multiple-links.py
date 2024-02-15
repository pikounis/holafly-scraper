import requests
from bs4 import BeautifulSoup
import json

# List of URLs to fetch the HTML content from
urls2 = [
    'https://esim.holafly.com/shop/?first_letter=A&last_letter=B',
    'https://esim.holafly.com/shop/?first_letter=C&last_letter=E',
    'https://esim.holafly.com/shop/?first_letter=G&last_letter=H',
    'https://esim.holafly.com/shop/?first_letter=I&last_letter=M',
    'https://esim.holafly.com/shop/?first_letter=L&last_letter=N',
    'https://esim.holafly.com/shop/?first_letter=P&last_letter=R',
    'https://esim.holafly.com/shop/?first_letter=S&last_letter=S',
    'https://esim.holafly.com/shop/?first_letter=T&last_letter=Z'
]

urls = [
    'https://esim.holafly.com/shop/?first_letter=S&last_letter=S'
]

# Initialize a list to hold the extracted countries and links from all URLs
all_countries_links = []

# Iterate over each URL in the list
for url in urls:
    # Use requests to fetch the content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all anchor tags with class 'nav-link'
    anchors = soup.find_all('a', class_='nav-link')

    # Extract the countries and links, appending them to the all_countries_links list
    for anchor in anchors:
        all_countries_links.append({'country': anchor.text.strip(), 'link': anchor['href']})

# Remove duplicates
seen = set()
unique_countries_links = [x for x in all_countries_links if x['country'] not in seen and not seen.add(x['country'])]

# Convert the combined list to JSON format
json_data = json.dumps(unique_countries_links, indent=4)

# Define the JSON file name
file_name = 'combined_countries_links.json'

# Save the JSON data to the file
with open(file_name, 'w') as file:
    file.write(json_data)

print(f'JSON data has been saved to {file_name}')
