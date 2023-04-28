# enumurate
# enumerate(iterable, start=0)
# Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.

fruits = ['apple', 'banana', 'orange']
# for idx, fruit in enumerate(fruits):
#     print(idx)
#     print(fruit)

for x in enumerate(fruits):
    print(type(x))
