class MyClass:
    # def __str__(self):
    #     return "MyClassの__str__メソッドが実行されました。"
    pass


mc = MyClass()
print(mc)
print(1) # 1.__str__()と同じ
print("abc") # "abc".__str__()と同じ
print([1, 2, 3]) # [1, 2, 3].__str__()と同じ
print({"a": 1, "b": 2}) # {"a": 1, "b": 2}.__str__()と同じ

# __str__メソッドは、print()関数やstr()関数でオブジェクトを文字列に変換する際に呼び出されます。
# このように、特定の関数が呼び出されるタイミングでメソッドを実行することを、メソッドのオーバーライドと呼びます。

# __str__メソッドは、print()関数やstr()関数でオブジェクトを文字列に変換する際に呼び出されます。