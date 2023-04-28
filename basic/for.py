# forループ
fruits = ['apple', 'banana', 'orange', 'grape', 'peach']

# for fruit in fruits:
#     print(f"I love {fruits}")


# for char in "hello world!":
#     print(f"char: {char}")


# challenge1
# like = input(f"好きなフルーツを入力してください：")
# for fruit in fruits:
#     if like == fruit:
#         print(f"{fruit}は好き")
#     else:
#         print(f"{fruit}は嫌い")

#challenge2
favorite_fruits = []
non_favorite_fruits = []
for fruit in fruits:
    like = input(f"{fruit}は好きですか？(y/n)")
    if like == "y":
        favorite_fruits.append(fruit)
    else:
        non_favorite_fruits.append(fruit)
print(f"好きなフルーツ：{favorite_fruits}")
print(f"嫌いなフルーツ：{non_favorite_fruits}")