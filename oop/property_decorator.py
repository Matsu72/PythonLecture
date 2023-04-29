class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        print("get_age()が呼び出されました")
        return self._age

    @age.setter
    def age(self, age):
        print("set_age()が呼び出されました")
        if age < 0:
            raise ValueError("年齢は正の数で指定してください")
        self._age = age

    # age = property(get_age, set_age)

john = Person("John", 18)
print(john.age)
john.age = -10