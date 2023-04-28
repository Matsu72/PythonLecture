# type()
hello_type = type("Hello")
print(hello_type)

figure = 3
print(type(figure))
print(type(3.14))
print(type(True))
print(type(float(figure)))

# what is id()?
# id()はオブジェクトのメモリ上のアドレスを返す
# 例えば、helloとhello2は同じ文字列を参照しているので、同じアドレスを返す


# id()
hello = "hello"
hello2 = "hello"
world = "world"
print(id(hello))
print(id(hello2))
print(id("hello"))
print(id(world))