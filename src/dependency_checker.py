import os 
import json 
import pathlib
from typing import Tuple, List
import zipfile
import uuid
import chardet
# from decouple import config
# packages = []

import sys
# curr_dir = pathlib.Path(__file__).parent.resolve()
# sys.path.append(curr_dir)
# sys.path.append("..")
# print(sys.path)
# print(pathlib.Path(__file__).parent.resolve())
# import DC.dependency_checker
# import DE.dependency_extractor
# from DC import dependency_checker



curr_path = os.path.dirname(__file__)
print(curr_path_DE := os.path.join(curr_path,"..", "DE"))
print(curr_path_DC := os.path.join(curr_path,"..", "DC"))
print(curr_path_common := os.path.join(curr_path,"..", "common"))

sys.path.extend([curr_path_DE, curr_path_DC, curr_path_common])

import dependency_checker, dependency_extractor, filter_file


# ANSI
# UTF-16 LE
# UTF-16 BE
# UTF-8 
# UTF-8 with BOM
# GIT or maybe VSCode changes the encoding of requirements file so I have added all encodings if one fails other will apply
def read_file_legacy(file:str)-> str:
    '''
    Description: 
        Read the file with appropriate encoding

    Params: 
        file: path of the file

    Return:
        returns the content of file is string format
    '''
    data = ''
    encodings = ["utf-8", "utf-16 LE" ,"ANSI", ]
    for encode in encodings:
        try:
            with open(file, 'r',encoding=encode) as f: 
                data = f.read()
                return data 

        except:
            print(f)
            print(f"******************  I AM IN EXCEPT BLOCK FOR FILE {file} with encondings: {encode}  ****************")

            continue
    
        # print(data)
        # print(type(data))


def read_file(file_path):
    '''
    Description: 
        Read the file with appropriate encoding

    Params: 
        file: path of the file

    Return:
        returns the content of file is string format
    '''
    # Detect the encoding of the file
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())

    # Use the detected encoding to read the file
    encoding = result['encoding']
    confidence = result['confidence']

    if confidence > 0.5:  # You can adjust the confidence threshold as needed
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
        return content
    else:
        # TODO: Log -C- File cannot be read using above encodings

        print(f"Low confidence in detected encoding ({confidence}). Manual inspection may be needed.")

def generate_unique_name(file_name:str)-> str:
    return file_name +  str(uuid.uuid4) 


# def create_directory(zip_file_name:str)-> bool:
#     try: 
#         os.makedirs(os.path.join(config("uploadPath"), zip_file_name), exist_ok=True)
#         return True
#     except: 
#         # TODO: Log -C- Folder not created, maybe because of write permissions  
#         # Due to write permissions
#         return False

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
    '''
    Description: 
        Checks name and extension of file from file path

    Params: 
        path: file path

    Return:
        returns tuple of name and extension
    '''
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


# def filter_requirements_files(filePath) -> bool: 
#     return True if pathlib.Path(filePath).suffix == '.txt' and ("requirements" or "requirement") in pathlib.Path(filePath).stem.lower()  else False
    

def read_packages(data):
    splitted_data = data.split("\n")
    non_version_packages = set()
    packages = [{i[0]:i[1]} for i in [i.split("==") if "==" in i else non_version_packages.add(i) for i in splitted_data] if i is not None]
    return packages

def aggregator(input):
    if check_type(input):
        paths, names = parse_files(input)
        files_paths = list(map(get_files_paths,paths,names))
        req_files = list(filter(filter_file.filter_requirements_files,files_paths))
        print(req_files)
        requirements = list(map(read_file,req_files))
        packages = list(map(read_packages,requirements))
        print(packages)
        # ab = 

    else:
        print("THIS IS ZIP FILE")



if __name__ == "__main__":
    input = r"D:\2022\Python-DCV\test_data\test_directory_1"
    aggregator(input)
    