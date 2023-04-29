class MyClass(object):
    def __init__(self) -> None:
        pass

    def mymethod(self):
        print("This is my method")

    @staticmethod
    def mystaticmethod():
        print("This is my static method")

# c = MyClass()
# c.mymethod()
MyClass.mystaticmethod()