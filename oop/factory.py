import time

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def create_from_dob(cls, name, year, month, day):
        age = cls.calc_age(year, month, day)
        return cls(name, age)
    
    @staticmethod
    def calc_age(year, month, day):
        # 現在の年月日を取得
        today = time.localtime()
        # 年齢を計算
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, day))
        return age
    
    

john = Person.create_from_dob("John", 1999, 12, 1)
print(john.name)
print(john.age)