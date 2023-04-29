class Person(object):
    num_legs = 2
    count = 0
    # constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def work(self):
        print(f"{self.name} is working")
    
    def run(self):
        print(f"{self.name} is running")


John = Person("John", "28", "male")
Taro = Person("Taro", "18", "male")
Emma = Person("Emma", "40", "female")

# インスタンスメソッドの呼び出し
John.myfunc()
print(John.name)
print(John.age)
John.work()
Emma.run()

Person.num_legs = 19
print(John.num_legs)
print(Taro.num_legs)
print(Person.count)