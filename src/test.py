# def read_file(file:str) -> str:
#     data = ''
#     with open(file, 'r', encoding='utf-16 LE') as file: 
#         data = file.read()
#         # print(data)
#         # print(type(data))
#     return data 


import chardet

def read_file(file_path):
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
        print(f"Low confidence in detected encoding ({confidence}). Manual inspection may be needed.")

# Example usage
file_path = 'D:\\2022\\Python-DCV\\test_data\\test_directory_1\\src\\requirements_2.txt'
file_content = read_file(file_path)
print(file_content)


# def read_packages(data):
#     splitted_data = data.split("\n")
#     non_version_packages = set()
#     packages = [{i[0]:i[1]} for i in [i.split("==") if "==" in i else non_version_packages.add(i) for i in splitted_data] if i is not None]
#     return packages

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