import traceback

bill ={"burger":500, "pizza":1000, "coke":200, "fries":300}

def split_bill(bill):
    num = input("How many people are there? ")
    try:
        each = bill / int(num)
    except ZeroDivisionError:
        print("Number of people cannot be zero")
    else:
        print(f"Each person should pay: {each}")

def check(bill):
    total_bill = sum(bill.values())
    try:
        split_bill(total_bill)
    except ValueError:
        traceback.print_exc()
        print("Please enter a valid number")

if __name__ == "__main__":
    check(bill)
    print("このプログラムは正常に終了しました")