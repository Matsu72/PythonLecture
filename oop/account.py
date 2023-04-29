import time

class Account(object):
    count = 0
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_number = Account.count
        self.show_balance()
        self.transaction_history = []
        Account.count += 1

    def withdraw(self, amount):
        if self.balance < amount:
            print("残高不足です")
        else:
            self.balance -= amount
            print(f"{amount}円引き出しました")
            self.show_balance()
            self.add_transaction_history(-amount)
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}円預けました")
        self.show_balance()
        self.add_transaction_history(amount)

    def transfer(self, other, amount):
        if self.balance < amount:
            print("残高不足です")
        else:
            self.balance -= amount
            other.balance += amount
            print(f"{self.name}から{other.name}へ{amount}円振り込みました")
            print(f"{self.name}の残高は{self.balance}円です")
            print(f"{other.name}の残高は{other.balance}円です")

    def show_balance(self):
        print(f"{self.name}の残高は{self.balance}円です")

    def add_transaction_history(self, price):
        transaction = {
            "withdraw / deposit": price,
            "balance": self.balance,
            "time": Account.get_time_str()
        }
        self.transaction_history.append(transaction)
    
    @staticmethod
    def get_time_str():
        currenct_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(currenct_time)
    
    def show_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)


John = Account(1000, "John")
Taro = Account(2000, "Taro")
Emma = Account(3000, "Emma")

# Emma.transfer(John, 500)

John.withdraw(500)
Taro.deposit(1000)
Emma.withdraw(4000)
John.deposit(2000)
print(John.account_number)

print(John.transaction_history)
print(John.show_transaction_history())
