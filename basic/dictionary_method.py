fruits_color = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

# if "peach" in fruits_color:
#     print("peach is a key of fruits_color")
# else:
#     print("peach is not a key of fruits_color")

# fruit = input("フルーツの名前を指定してください>>")
# print(fruits_color.get(fruit, "Nothing"))

# .update()
fruits_color2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_color.update(fruits_color2)
print(fruits_color)