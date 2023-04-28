# 参照渡し <-> 値渡し
# 参照渡し: 関数に渡した引数の値を関数内で変更すると、関数を呼び出した側の変数の値も変更される
# 値渡し: 関数に渡した引数の値を関数内で変更しても、関数を呼び出した側の変数の値は変更されない

# def add_nums(a, b):
#     print(f"第一引数aのid: {id(a)}")
#     print(f"第二引数bのid: {id(b)}")
#     return a + b

# one = 1
# two = 2
# print(f"oneのid: {id(one)}")
# print(f"twoのid: {id(two)}")
# print(add_nums(one, two))

# この関数は、引数の値を変更することはない
# pythonは全て参照渡し

# def add_one(num):
#     print(f"変更前のid: {id(num)}")
#     num += 1
#     print(f"変更後のid: {id(num)}")
#     return num
# one = 1
# print(id(one))
# print(f"関数呼び出し前のone: {id(one)}")
# # add_one(one)
# one = add_one(one)
# print(f"関数呼び出し後のone: {id(one)}")

def add_fruit(fruits, fruit):
    print(f"変更前のid: {id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のid: {id(fruits)}")
    return fruits

fruits = ["apple", "banana"]
my_fruit = "lemon"
print(f"関数呼び出し前のfruits: {id(fruits)}")
add_fruit(fruits, my_fruit)
print(f"関数呼び出し後のfruits: {id(fruits)}")
print(fruits)