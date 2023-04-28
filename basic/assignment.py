# 変数へ代入
hello = 'hello'
world = 'world'

print(hello)
print(world)

# format
print("{} {}".format(hello, world))  # hello world

name = "John"
print("Hey {}, How are you doing?".format(name))

# fstring
print(f"Hello, {name}")

# fstringの中で計算もできる
product = "apple"
print(f"The product name is {product}")

x = 10
y = 5
result = f"{x} + {y} = {x + y}"
print(result)   