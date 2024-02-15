import requests
from bs4 import BeautifulSoup

# Example URL from your JSON data
url = 'https://esim.holafly.com/esim-albania/'  # Replace with the actual link

# Fetch the webpage content
response = requests.get(url)
page_content = response.text

# Parse the HTML content
soup = BeautifulSoup(page_content, 'html.parser')

# Find the specific div containing the data you're interested in
product_variation = soup.find('div', class_='product-variation unlimited-data')

# Extract the required elements
data_volume = product_variation.find('span', class_='variation_data').text
duration = product_variation.find('strong', class_='variation_days').text
price_info = product_variation.find('bdi').text

print(f"Data Volume: {data_volume}, Duration: {duration}, Price: {price_info}")
