import requests
from bs4 import BeautifulSoup
import json

# Load the JSON data from the file
file_path = 'holafly_deeplinks.json'  # Update this path
with open(file_path, 'r') as file:
    links_data = json.load(file)

# Initialize a list to hold the extracted data
extracted_data = []

# Iterate over each country link in the JSON data
for entry in links_data:
    url = entry['link']
    country = entry['country']

    # Fetch the webpage content
    response = requests.get(url)
    page_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(page_content, 'html.parser')

    # Initialize a list to store packages info for the current country
    packages_data = []

    # Use a set to track unique package attributes to prevent duplicates
    seen_packages = set()

    # Find all specific divs and extract the required elements
    product_variations = soup.find_all('div', class_='product-variation unlimited-data')
    for product_variation in product_variations:
        data_volume = product_variation.find('span', class_='variation_data').text.strip() if product_variation.find(
            'span', class_='variation_data') else 'Not found'
        duration = product_variation.find('strong', class_='variation_days').text.strip() if product_variation.find(
            'strong', class_='variation_days') else 'Not found'

        # Extract price and remove the currency symbol if present
        price_info = product_variation.find('bdi').text.strip() if product_variation.find('bdi') else 'Not found'
        price_info = price_info.replace('\u20ac', '').strip()  # Remove the Euro symbol

        currency_symbol = soup.find('div', class_='currency_symbol').text.strip() if soup.find('div',
                                                                                               class_='currency_symbol') else 'Not specified'

        # Create a unique key for each package to prevent duplicates
        package_key = (data_volume, duration, price_info, currency_symbol)

        # Check if the package is unique before adding
        if package_key not in seen_packages:
            seen_packages.add(package_key)
            package_data = {
                'data_volume': data_volume,
                'duration': duration,
                'price': price_info,  # Cleaned price without the currency symbol
                'currency': currency_symbol  # Include the currency information
            }

            # Add the package info to the country's list of packages
            packages_data.append(package_data)

    # Add the extracted information for the country, including all packages, to the list
    extracted_data.append({'country': country, 'url': url, 'packages': packages_data})

# Save the extracted data in JSON format to a file named results.json
results_file_path = 'results.json'  # Adjust this path as needed
with open(results_file_path, 'w') as outfile:
    json.dump(extracted_data, outfile, indent=4)

print(f'Data saved to {results_file_path}')
