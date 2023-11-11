def read_file(file:str) -> str:
    data = ''
    with open(file, 'r', encoding='utf-8 LE') as file: 
        data = file.read()
        # print(data)
        # print(type(data))
    return data 

def read_packages(data):
    splitted_data = data.split("\n")
    non_version_packages = set()
    packages = [{i[0]:i[1]} for i in [i.split("==") if "==" in i else non_version_packages.add(i) for i in splitted_data] if i is not None]
    return packages

# data1 = read_file(r"D:\2022\Python-DCV\test_data\requirements_2.txt")
data2 = read_file(r"D:\\2022\\Python-DCV\\test_data\\test_directory_1\\src\\requirements_2.txt")
print(data2)

print(type(data2))
print("REPRRR******************8")
# print(repr(data1))
# print(repr(data2))

# l1 = []
# l1.append(data1)
# l1.append(data2)

# print(l1)

# packages = read_packages(data)
# print(packages)