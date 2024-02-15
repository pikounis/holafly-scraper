# Convert the given HTML snippet to a JSON object with country names and links

html_snippet = """
<ul id="menu-todos-los-productos" class="second-menu__main-nav menu-todos-destinos"><a class="nav-link" href="https://esim.holafly.com/esim-albania/">Albania</a><a class="nav-link" href="https://esim.holafly.com/esim-algeria/">Algeria</a><a class="nav-link" href="https://esim.holafly.com/esim-andorra/">Andorra</a><a class="nav-link" href="https://esim.holafly.com/esim-argentina/">Argentina</a><a class="nav-link" href="https://esim.holafly.com/esim-armenia/">Armenia</a><a class="nav-link" href="https://esim.holafly.com/esim-aruba/">Aruba</a><a class="nav-link" href="https://esim.holafly.com/esim-asia/">Asia</a><a class="nav-link" href="https://esim.holafly.com/esim-australia/">Australia</a><a class="nav-link" href="https://esim.holafly.com/esim-austria/">Austria</a><a class="nav-link" href="https://esim.holafly.com/esim-azerbaijan/">Azerbaijan</a><a class="nav-link" href="https://esim.holafly.com/esim-bahrain/">Bahrain</a><a class="nav-link" href="https://esim.holafly.com/esim-bangladesh/">Bangladesh</a><a class="nav-link" href="https://esim.holafly.com/esim-barbados/">Barbados</a><a class="nav-link" href="https://esim.holafly.com/esim-belarus/">Belarus</a><a class="nav-link" href="https://esim.holafly.com/esim-belgium/">Belgium</a><a class="nav-link" href="https://esim.holafly.com/esim-bosnia-and-herzegovina/">Bosnia and Herzegovina</a><a class="nav-link" href="https://esim.holafly.com/esim-botswana/">Botswana</a><a class="nav-link" href="https://esim.holafly.com/esim-brazil/">Brazil</a><a class="nav-link" href="https://esim.holafly.com/esim-brunei/">Brunei</a><a class="nav-link" href="https://esim.holafly.com/esim-bulgaria/">Bulgaria</a><li> <a style="text-decoration: underline;font-weight: bold;" href="https://esim.holafly.com/shop/?first_letter=A&amp;last_letter=B">See all</a></li></ul>
"""

from bs4 import BeautifulSoup
import json

# Parse the HTML snippet
soup = BeautifulSoup(html_snippet, 'html.parser')

# Extract all anchor tags
anchors = soup.find_all('a', class_='nav-link')

# Create a list of dictionaries for each country and its link
countries_links = [{'country': anchor.text.strip(), 'link': anchor['href']} for anchor in anchors]

# Convert list to JSON
json_data = json.dumps(countries_links, indent=4)

# Save the JSON data to a file
file_path = './data/countries_links.json'

with open(file_path, 'w') as file:
    file.write(json_data)

file_path
