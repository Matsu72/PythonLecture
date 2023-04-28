# in演算子
fruits = ['apple', 'banana', 'orange', 'grape', 'peach']

# print('apple' not in fruints)

# print("h" in "hello")

#リストの中身を削除する
# fruints.remove('apple')

# challenge

input_fruit = input("フルーツを入力してください：")
if input_fruit in fruits:
    print(f"{input_fruit}ですね、差し上げますよ")
    fruits.remove(input_fruit)
else:
    print(f"{input_fruit}ですね、仕入れました！")
    fruits.append(input_fruit)
print(fruits)