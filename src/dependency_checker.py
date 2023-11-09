import os 
import json 
import pathlib
from typing import Tuple, List
import zipfile
import uuid
from decouple import config
packages = []



def read_file(file:str) -> str:
    data = ''
    with open(file, 'r',encoding='utf-8', errors='ignore') as file: 
        data = file.read()
        print(data)
        print(type(data))
    return data 

def generate_unique_name(file_name:str)-> str:
    return file_name +  str(uuid.uuid4) 


def create_directory(zip_file_name:str)-> bool:
    try: 
        os.makedirs(os.path.join(config("uploadPath"), zip_file_name), exist_ok=True)
        return True
    except: 
        # TODO: Log -C- Folder not created, maybe because of write permissions  
        # Due to write permissions
        return False

def unzip(path, newDir):
     with zipfile.ZipFile(path, 'r') as zip:
    # printing all the contents of the zip file
            # zip.printdir()
        # if extractedDirPath == None : 
            # newDir,zipProjectName = making_new_DIR(folderName , filePath)
            # extracting files at default location
        print('Extracting Files: ' + newDir)
        zip.extractall(newDir)

def check_type(upload) -> bool:
    """
    Checks if the given input file is a folder or zipped file

    Parameters: 
        upload: path of uploaded folder/zippedfile

    Return: 
        'True' if it's folder and 'False' if i'ts zip file
    """
    return True if os.path.isdir(upload) else False


def get_name_n_extension(path:str) -> Tuple[str,str]: 
    return pathlib.Path(path).stem, pathlib.Path(path).suffix
    


def get_files_paths(root:list,file_names:list)-> List[int]:
    return os.path.join(root,file_names)
    # completePath = []
    # for index, files_name in enumerate(file_names):
    # # Getting complete path of all the files in the directory
    #     completePath.append(os.path.join(root[index], files_name))
    # return [os.path.join(root[index], file_name) for index, file_name in enumerate(file_names)]

def parse_files(path:str) -> Tuple[List[int], List[int]]:
    file_paths = [] 
    file_names = [] 

    for root, dirs, files in os.walk(path):
        for filename in files:
            file_paths.append(root)
            file_names.append(filename)
    
    # print("** FILES PATHS**")
    # print(file_paths)
    # print("** FILE NAMES **")
    # print(file_names)
    return file_paths,file_names


def filter_requirements_files(filePath) -> bool: 
    return True if pathlib.Path(filePath).suffix == '.txt' and ("requirements" or "requirement") in pathlib.Path(filePath).stem.lower()  else False
    

def read_packages(data):
    splitted_data = data.split("\n")
    non_version_packages = set()
    packages = [{i[0]:i[1]} for i in [i.split("==") if "==" in i else non_version_packages.add(i) for i in splitted_data] if i is not None]
    return packages

def aggregator(input):
    if check_type(input):
        paths, names = parse_files(input)
        files_paths = list(map(get_files_paths,paths,names))
        # print(files_paths)
        req_files = list(filter(filter_requirements_files,files_paths))
        # print(req_files)
        requirements = list(map(read_file,req_files))
        print(requirements)
        # requirements_files = map(filter_requirements_files,files_paths)
        print("THIS IS FOLDER")

    else:
        print("THIS IS ZIP FILE")



if __name__ == "__main__":
    input = r"D:\2022\Python-DCV\test_data\test_directory_1"
    aggregator(input)