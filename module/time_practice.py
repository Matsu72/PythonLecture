import time
from functools import lru_cache

# print(time.time())
# print(time.time()/(60*60*24*365))

@lru_cache(maxsize=None)
def fib(n):
    print(f"fibonacci with {n} is runninng...")
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

# before = time.time()
# # 処理  
# fib(30)
# after = time.time()
# print(f"recursive: {after - before: 2f} sec.")

# .ctime()は、引数に指定した秒数を、人間が読める形式に変換してくれる

# print(time.ctime())

# localtime = time.localtime()
# print(localtime.tm_year)

# # time.sleep()は、引数に指定した秒数だけ、処理を停止する

# sec = 10
# print(f"{sec}秒間、処理を停止します")
# time.sleep(sec)
# print("処理を再開します")

def timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before: 2f} sec.")
    return inner

@timer
def lazy_func(sec=3):
    print("lazy_func() is running...")
    time.sleep(sec)
    print("lazy_func() is done")

lazy_func()

