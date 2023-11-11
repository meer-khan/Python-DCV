import sys 
import os 
import pathlib
print(os.path.abspath(__file__))
print(pathlib.Path(__file__))

# curr_path = pathlib.Path(__file__)
# curr_path = os.path.join(os.path.dirname(__file__), '..', 'src', "..", "DC")
# print(curr_path)
# path_to_DC = os.path.join(curr_path,"..","src","..", "DC")
# print(path_to_DC)
# sys.path.append(curr_path)
# print(path_to_DC)
import DC.dependency_checker


