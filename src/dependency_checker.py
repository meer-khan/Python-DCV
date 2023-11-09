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

def unzip():
    pass

def check_type(upload):
    return True if os.path.isdir(upload) else False

def get_extension(): 
    pass

def parse_files():
    pass

def get_requirements_files(): 
    pass

def read_packages(data):
    splitted_data = data.split("\n")
    non_version_packages = set()
    packages = [{i[0]:i[1]} for i in [i.split("==") if "==" in i else non_version_packages.add(i) for i in splitted_data] if i is not None]
    return packages

def aggregator():
    if check_type(input):
        files = parse_files(input)
        requirements_files = map(get_requirements_files,files)
        
    else:
        pass
    # data = read_file()
    print("################# PACKAGES #########################")
    # print(packages)
    print("################# NO VERSION #########################")
    # print(non_version_packages)


if __name__ == "__main__":
    input = ""
    aggregator(input)