class MyClass(object):
    classmethod_count = 0
    def __init__(self) -> None:
        pass

    def mymethod(self):
        print("This is my method")

    @staticmethod
    def _mystaticmethod():
        print("This is my static method")

    @classmethod
    def _myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is my class method and now the count is {cls.classmethod_count}")

c = MyClass()
c.mymethod()
MyClass._myclassmethod()
