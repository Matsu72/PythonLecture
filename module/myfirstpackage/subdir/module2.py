from .. import module1

def myfunc():
    print("This is myfunc from module2.py")


def myfunc2():
    print("This is myfunc2 from module2.py")
    module1.myfunc()