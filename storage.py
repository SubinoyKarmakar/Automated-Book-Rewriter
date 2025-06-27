import json
import os

# Function to save a version of the content (original, AI, human-edited) as a JSON file in 'data' folder.
def save_version(data, version_name):
    os.makedirs("data", exist_ok=True)      #Create 'data' folder if it doesn't exist
    file_path = f"data/{version_name}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)     #Save JSON with indentation for readability

#This function will load and return the content dictionary from a saved JSON file in the 'data' directory. Returns None if file not found.
def load_version(version_name):
    file_path = f"data/{version_name}.json"

    if not os.path.exists(file_path):
        return None     # It will return Version file doesn't exist

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)      #It will load and return JSON content as Python dictionary
