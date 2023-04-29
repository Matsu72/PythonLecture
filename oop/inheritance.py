class Animal(object):
    def __init__(self, name):
        self.name = name
        print("Animal.__init__が呼び出されました")

    def eat(self, food):
        print('{} is eating {}.'.format(self.name, food))


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)
        print("Dog.__init__が呼び出されました")

    def bark(self):
        print('Bow wow!')


pochi = Dog('Pochi')
pochi.eat('beef')
