# range(18)

def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


# mr = myrange(10)
# print(type(mr))

# for i in mr:
#     print(i)


def myevenrange(start):
    start = start
    while start > 0:
        if start % 2 == 0:
            yield start
        start -= 1

for i in myevenrange(10):
    print(i)