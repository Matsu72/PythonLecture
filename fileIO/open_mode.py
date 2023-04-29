import os

file_path = os.path.dirname(os.path.abspath(__file__)) + "/"
file_name = file_path + "pep8.txt"

# # mode = a : append mode
# with open(file_path + "writing_file.txt", mode="a") as f:
#     f.write("Test\n I am writing file\n")

# mode = r+ : read and write mode
# with open(file_path + "writing_file.txt", mode="r+") as f:
#     f.write("You can write and read with r+ mode\n")
#     f.seek(0)
#     print(f.read())
#     f.write("This should be the last line\n")

# mode = w+ : write and read mode
# with open(file_path + "writing_file.txt", mode="w+") as f:
#     f.write("You can write and read with w+ mode\n")
#     # f.seek(0)
#     print(f.read())
#     f.write("This should be the last line\n")
#     print(f.read())

# mode = a+ : append and read mode
with open(file_path + "writing_file.txt", mode="a+") as f:
    f.write("You can write and read with a+ mode\n")
    f.seek(0)
    print(f.read())
    f.write("This should be the last line\n")
    f.seek(0)
    print(f.read())