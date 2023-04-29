import os


print(os.path.dirname(os.path.abspath(__file__)))
file_name = os.path.dirname(os.path.abspath(__file__))+ "/pep8.txt"

# try:
#     f = open(file_name)
#     for line in f:
#         print(line, end="")
# finally:
#     f.close()

# with statement
with open(file_name) as f:
    for line in f:
        print(line, end="")
