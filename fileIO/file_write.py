import os

# for文でループで回す
print(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.dirname(os.path.abspath(__file__)) + "/"
file_name = file_path + "pep8.txt"
print(file_path)

with open(file_path + "writing_file.txt", mode="w") as f:
    f.write("Test\n I am writing file\n")
    
# truncated mode
# with open(file_path + "writing_file.txt", mode="w") as f: