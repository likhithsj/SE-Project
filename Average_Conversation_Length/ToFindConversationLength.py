import json

# Specify the path to your JSON file
json_file_path = 'snapshot_20230831/prsharing.json'

# Load JSON data from the file with explicit encoding
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the "chats" array
chats = data.get("chats", [])

# Calculate the average number of elements in each list
average_elements = sum(len(chat) for chat in chats) / len(chats)

print(f"Average number of elements in each list: {average_elements}")
