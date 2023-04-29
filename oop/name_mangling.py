class Accout:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if self.__balance < amount:
            raise RuntimeError("残高不足")
        self.__balance -= amount
        self.show_balance()

    def show_balance(self):
        print(f"残高は{self.__balance}円です")

myaccount = Accout(10000)
print(myaccount._Accout__balance)