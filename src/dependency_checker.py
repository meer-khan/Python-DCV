import os 
import json 
import pathlib


packages = {}



def read_file():
    with open("../test_data/requirements.txt", 'r',encoding='utf-8', errors='ignore') as file: 
        lines = file.read()
        print(lines)
        print(type(lines))





# Parse the lines and populate the dictionary.
# for line in lines:
#     parts = line.split(' = ')
#     print(parts)
    # package_name, package_info = parts[0], parts[1] if len(parts) > 1 else None
    # packages[package_name] = package_info


# print(packages)
# Convert the dictionary to a JSON string.
# json_data = json.dumps(packages, indent=4, ensure_ascii=False)

# Print or save the JSON data as needed.
# print(json_data)