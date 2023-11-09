import os 
import json 
import pathlib


packages = []



def read_file():
    data = ''
    with open("../test_data/requirements_1.txt", 'r',encoding='utf-8', errors='ignore') as file: 
        data = file.read()
        print(data)
        print(type(data))
    return data 



data = read_file()

splitted_data = data.split("\n")
non_version_packages = set()
# l1 = []
# l2 = []
# for i in splitted_data:
#     if "==" in i:
#         l1.append(i.split("=="))
#     else: 
#         non_version_packages.add(i)
    
#     for i in l1: 
#         l2.append({i[0]:i[1]} )
# print("_____________________l1_________________")
# print(l1)
# print("_____________________l2_________________")
# print(l2)

packages = [{i[0]:i[1]} for i in [i.split("==") if "==" in i else non_version_packages.add(i) for i in splitted_data] if i is not None]
# print([i.split("==") if "==" in i else non_version_packages.append(i) for i in splitted_data])
# l2, non_version_packages = ([i[0]: i[1] for i in item.split("==")] for item in splitted_data if "==" in item), [item for item in splitted_data if "==" not in item]

print("################# PACKAGES #########################")
print(packages)
print("################# NO VERSION #########################")
print(non_version_packages)
    






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