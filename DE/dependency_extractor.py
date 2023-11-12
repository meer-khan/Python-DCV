import re, os ,pathlib, sys
# sys.path.append("..")
# sys.path.append()
# from DC import dependency_checker

curr_path = os.path.dirname(__file__)
print(curr_path)
print(curr_path := os.path.join(curr_path,"..", "DC"))
# print(curr_path)
sys.path.append(curr_path)
import dependency_checker



