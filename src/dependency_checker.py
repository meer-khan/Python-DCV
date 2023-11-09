import os 
import json 
import pathlib
from typing import Tuple, List

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


def get_all_files_paths(root:list,file_names:list)-> List[int]:
    completePath = []
    for index, files_name in enumerate(file_names):
    # Getting complete path of all the files in the directory
        completePath.append(os.path.join(root[index], files_name))

    return completePath

def parse_files(path:str) -> Tuple(List[int], List[int]):
    file_paths = [] 
    file_names = [] 
    for root, dirs, files in os.walk(path):
        print(f"ROOT: {root}")
        print(f"DIRS: {dirs}")
        print(f"FILES: {files}")
        # file_names.extend(files)
        # file_paths.append(root)
        for filename in files:
            file_paths.append(root)
            file_names.append(filename)
    
    print("** FILES PATHS**")
    print(file_paths)
    print("** FILE NAMES **")
    print(file_names)
    return file_paths,file_names
def get_requirements_files(): 
    pass

def read_packages(data):
    splitted_data = data.split("\n")
    non_version_packages = set()
    packages = [{i[0]:i[1]} for i in [i.split("==") if "==" in i else non_version_packages.add(i) for i in splitted_data] if i is not None]
    return packages

def aggregator(input):
    if check_type(input):
        paths, names = parse_files(input)
        requirements_files = map(get_requirements_files,paths)

    else:
        pass
    # data = read_file()
    print("################# PACKAGES #########################")
    # print(packages)
    print("################# NO VERSION #########################")
    # print(non_version_packages)


if __name__ == "__main__":
    input = r"D:\2022\Python-DCV\test_data\test_directory_1"
    aggregator(input)