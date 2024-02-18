import re, os ,pathlib, sys
curr_path = os.path.dirname(__file__)
# print(curr_path)
print(curr_path := os.path.join(curr_path,"..", "DC"))
sys.path.append(curr_path)
import dependency_checker
from icecream import ic

import ast

'''
1. Extract single imports e.g. import pandas - #*Done
2. Extract single imports with alias e.g. import pandas as pd - #*Done
3. Extract multiple imports e.g. import os, sys - #*Done
4. Extract from single import e.g. from pandas import read_csv  # TODO: ^from\s+(\w+)\s+import\s+(\w+)$
    4.1 Extract package name e.g. pandas
    4.2 Extract function/class/module used by from import e.g. read_csv 
5. Extract from multiple import e.g. from pandas import read_csv, DataFrame, to_csv   #TODO: ^from\s+(\w+)\s+import\s+(\w+\s*,.*)$
    5.1 Extract package name e.g. pandas  #TODO:above regex will extract package name as group
    # 5.1 Extract function/class/module used by from import e.g. read_csv, DataFrame, to_csv seperate them out # TODO: do it using , seperator
6. Extract from multi package single class e.g. from flaskapi.sqlalchemy.request import sqlalchemy_request  #TODO: ^from\s+(\w+\.[\w\.]+)\s+import\s+(\w+)$ - 
7. Extract from multi package multi class e.g. from flaskapi.sqlalchemy.request import sqlalchemy_request, sqlalchemy_response #TODO:REVISED : ^from\s+(\w+\.[\w\.]+)\s+import\s+(\w+,\s*[\w\s,]+)$ - Extract after comman splitting
8. Extract bracket/multiline import e.g. 
                            from pandas import (read_csv, DataFrame
                                                to_csv) #TODO: ^from\s+\w+[\w\.]+\s+import\s+\([\w,\s]+\) - REVISED: ^from\s+(\w+[\w\.]+)\s+import\s+\(([\w,\s]+)\)$
9. Extract from multi package multi class bracket/multiline 
                            e.g. from flaskapi.sqlalchemy.request import (sqlalchemy_request, 
                                                                            sqlalchemy_response) #TODO ^from\s+(\w+[\w\.]+)\s+import\s+\(([\w,\s]+)\)$
10.  Extract brackets/multiline import e.g. import (os,sys, #!THIS SYNTAX DOES NOT EXISTS in PYTHON
                                                    pathlib, re) #TODO: ^import\s+\(([\w,\s]+)\)$ 

11. import single class with dot e.g. import fastapi.api #TODO: ^import\s+(\w+\.[\w.+]+)$
12. from single package single class with dot from fastapi import  fastapi.api.response  #!THIS SYNTAX DOES NOT EXISTS in PYTHON

'''

import re
import os.path


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content


def import_extractor(regex, content): 
    pattern = re.compile(regex, re.MULTILINE)
    matches = pattern.findall(content)
    # print("multi Imports Full Sat: ", matches)
    return matches
    

def extract_from_multi_package_multi_class(content): 
    matches = import_extractor(r"^^from\s+(\w+\.[\w\.]+)\s+import\s+(\w+,\s*[\w\s,]+)$", content)
    ic(matches)



# COMPLETE - 6
def extract_from_multi_package_single_class(content):
    matches = import_extractor(r"^from\s+(\w+\.[\w\.]+)\s+import\s+(\w+)$", content)
    ic(matches)

# COMPLETE - 5
def extract_from_multiple_imports(content):
    matches = import_extractor(r"^from\s+(\w+)\s+import\s+(\w+\s*,.*)$", content)    
    ic(matches)
    funs = matches[0][1].split(",")
    ic(funs)
    extract_data = {"lib": matches[0][0] , "fun": funs }
    ic(extract_data)

# COMPLETE - 4
def extract_from_single_import(content):
    full_statement = re.compile(r"^from\s+(\w+)\s+import\s+(\w+)$", re.MULTILINE)
    full_sat_matches = full_statement.findall(content)
    ic(full_sat_matches)

    # Get groups
    extract_data = [{"package":tup[0], "fun":tup[1]} for tup in full_sat_matches]
    ic(extract_data)

# COMPLETE - 3 
def extract_multiple_imports(content):
    # Get Complete Statement
    full_statement = re.compile("^import\s+\w+\s*,\s*\w+", re.MULTILINE)
    full_sat_matches = full_statement.findall(content)
    ic(full_sat_matches)

    # Get groups
    pattern = re.compile(r"^import\s+(\w+)\s*,\s*(\w+)", re.MULTILINE)
    matches = pattern.findall(content)
    ic(matches)

# COMPLETE - 2
def extract_single_imports_with_alias(content): 
    # Get complete statement
    full_statement = re.compile(r"^import\s+\w+\s+as\s+\w+", re.MULTILINE)
    full_sta_matches = full_statement.findall(content) 
    ic(full_sta_matches)
    # Get groups
    pattern = re.compile(r"^import\s+(\w+)\s+as\s+(\w+)" , re.MULTILINE)
    matches = pattern.findall(content)
    package_module = [{"package":pack, "alias":mod}for pack, mod in matches]
    ic(matches)
    ic(package_module)


# COMPLETED - 1
def extract_single_imports(content): 
    import_pattern = re.compile(r"^import\s+\w+$" , re.MULTILINE)
    import_matches = import_pattern.findall(content)

    fun_pattern = re.compile(r"^import\s+(\w+)$" , re.MULTILINE)
    fun_matches = fun_pattern.findall(content)
    ic(fun_matches, import_matches)


# Example usage:
file_path = r"D:\2022\Python-DCV\test_data\test_directory_1\src\imports.py"
content = read_file(file_path)
# print(content)
# imports = extract_multiple_imports(content)
extract_from_multi_package_multi_class(content)
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








