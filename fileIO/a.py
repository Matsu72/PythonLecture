import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
print(os.path.dirname(os.path.abspath(__file__)))