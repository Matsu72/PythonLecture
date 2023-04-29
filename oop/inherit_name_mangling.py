class Person:
    def __init__(self, name):
        self.name = name
        self.__mymethod()

    def mymethod(self):
        print("Personクラスのメソッドです")

    __mymethod = mymethod

class Baby(Person):

    def mymethod(self):
        print("Babyクラスのメソッドです")


taro_baby = Baby("太郎")
taro_person = Person("太郎")
taro_person.mymethod()



