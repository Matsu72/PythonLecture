def split_bill(price):
    num = input('How many people?')
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print('Invalid input.')
        print(e)
    except ValueError as e:
        print('Please input number')
        print(e)
    else:
        print(f"Each person needs to pay: {int(each)}")
    finally:
        print('Thank you for using our service.')

if __name__ == '__main__':
    split_bill(10000)

# try exceptの使い方
# try:
#     例外が発生する可能性のある処理
# except:
#     例外が発生した場合の処理
# else:
#     例外が発生しなかった場合の処理
# finally:
#     例外の有無に関わらず実行する処理

