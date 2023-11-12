import pathlib, os 
from typing import List

def filter_requirements_files(filePath:str) -> bool: 
    return True if pathlib.Path(filePath).suffix == '.txt' and ("requirements" or "requirement") in pathlib.Path(filePath).stem.lower()  else False


def filter_py_files(filePath:str) -> bool: 
    return True if pathlib.Path(filePath).suffix == '.py' else False
