import re, os ,pathlib, sys
curr_path = os.path.dirname(__file__)
# print(curr_path)
print(curr_path := os.path.join(curr_path,"..", "DC"))
sys.path.append(curr_path)
import dependency_checker


# def extract_imports(data:str):
#     pattern = re.Pattern()
#     pass

import ast

'''
1. Extract single imports e.g. import pandas - #*Done
2. Extract single imports with alias e.g. import pandas as pd - #*Done
3. Extract multiple imports e.g. import os, sys - #*Done
4. Extract from single import e.g. from pandas import read_csv  # TODO: ^from\s+(\w+)\s+import\s+(\w+)$
    4.1 Extract package name e.g. pandas
    4.2 Extract function/class/module used by from import e.g. read_csv 
5. Extract from multiple import e.g. from pandas import read_csv, DataFrame, to_csv   #TODO: ^from\s+(\w+)\s+import\s+\w+\s*,.*$
    5.1 Extract package name e.g. pandas  #TODO:above regex will extract package name as group
    # 5.1 Extract function/class/module used by from import e.g. read_csv, DataFrame, to_csv seperate them out # TODO: do it using , seperator
6. Extract from multi package multi class e.g. from flaskapi.sqlalchemy.request import sqlalchemy_request  #TODO: ^from\s+\w+\.[\w\s\.]+$
7. Extract bracket/multiline import e.g. 
                            from pandas import (read_csv, DataFrame
                                                to_csv) #TODO: ^import\s+\([\w,\s]+\)$
8. Extract brackets/multiline import e.g. import (os,sys,
                                                    pathlib, re)


'''

import re


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content


def extract_from_single_import(content):
    full_statement = re.compile("^import\s+\w+\s*,\s*\w+", re.MULTILINE)
    full_sat_matches = full_statement.findall(content)
    print("multi Imports Full Sat: ", full_sat_matches)

    # Get groups
    pattern = re.compile(r"^import\s+(\w+)\s*,\s*(\w+)", re.MULTILINE)
    matches = pattern.findall(content)
    print("Matches: ", matches)


def extract_multiple_imports(content):
    # Get Complete Statement
    full_statement = re.compile("^import\s+\w+\s*,\s*\w+", re.MULTILINE)
    full_sat_matches = full_statement.findall(content)
    print("multi Imports Full Sat: ", full_sat_matches)

    # Get groups
    pattern = re.compile(r"^import\s+(\w+)\s*,\s*(\w+)", re.MULTILINE)
    matches = pattern.findall(content)
    print("Matches: ", matches)

def extract_single_imports_with_alias(content): 
    # Get complete statement
    full_statement = re.compile(r"^import\s+\w+\s+as\s+\w+", re.MULTILINE)
    full_sta_matches = full_statement.findall(content) 
    print("Full Statement Match: ",full_sta_matches)
    # Get groups
    pattern = re.compile(r"^import\s+(\w+)\s+as\s+(\w+)" , re.MULTILINE)
    matches = pattern.findall(content)
    package_module = [{"package":pack, "module":mod}for pack, mod in matches]
    print("Group Matches: ",matches)
    print("Package and Module: ",package_module)


# COMPLETED
def extract_single_imports(content): 
    import_pattern = re.compile(r"^import\s+\w+$" , re.MULTILINE)
    import_matches = import_pattern.findall(content)

    fun_pattern = re.compile(r"^import\s+(\w+)$" , re.MULTILINE)
    print(fun_pattern)
    fun_matches = fun_pattern.findall(content)
    print("Matches:  ",fun_matches , "\nImport Patterns: ", import_matches)


# Example usage:
file_path = r"D:\2022\Python-DCV\test_data\test_directory_1\src\imports.py"
content = read_file(file_path)
print(content)
imports = extract_multiple_imports(content)
# print(imports)










def extract_imports_re(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression pattern to match import statements
    pattern = re.compile(r'^\s*(?:from\s+(\S+)\s+)?import\s+([^#\n]+)', re.MULTILINE)

    # Find all matches in the content
    matches = pattern.findall(content)

    # Extract module and names from the matches
    import_statements = []
    for module, names in matches:
        if module:
            # If "from" is present, add it to each imported name
            import_statements.extend(f"{module}.{name.strip()}" for name in names.split(','))
        else:
            # If "from" is not present, add the names directly
            import_statements.extend(names.split(','))

    return import_statements

# Example usage:

def extract_imports(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

    import_statements = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                import_statements.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            if module is not None:
                for alias in node.names:
                    import_statements.append(f"{module}.{alias.name}")

    return import_statements








