import json

# Step 1: Read the original JSON file
with open('holafly_object.json', 'r') as file:
    data = json.load(file)  # Step 2: Parse the JSON content

# Initialize a list to store the new dictionaries
new_data = []

# Step 3: Iterate over the list of dictionaries
for item in data:
    # Step 4: Extract "country" and "link" and construct the new dictionary
    new_dict = {
        "country": item["item_name"],
        "link": f"https://esim.holafly.com/{item['item_id']}/"
    }
    # Step 5: Append the new dictionary to the list
    new_data.append(new_dict)

# Step 6: Write the new list of dictionaries to a new JSON file
with open('holafly_deeplinks.json', 'w') as file:
    json.dump(new_data, file, indent=4)
