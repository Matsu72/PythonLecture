import os

# for文でループで回す
print(os.path.dirname(os.path.abspath(__file__)))
file_name = os.path.dirname(os.path.abspath(__file__))+ "/pep8.txt"

# with open(file_name) as f:
#     for line in f:
#         print(line, end="")

# read()で一気に読み込む
# with open(file_name) as f:
#     print(f.read())

# readline()で一行ずつ読み込む
# with open(file_name) as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line, end="")

# readlines()で一気に読み込む
with open(file_name) as f:
    l = f.readlines()
    print(l)
    for line in l:
        print(line, end="")

        