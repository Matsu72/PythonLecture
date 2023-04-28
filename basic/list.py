# リスト：複数のオブジェクトを格納する
# リストの作成
fruits = ['apple', 'orange', 'banana', 'peach']
print(fruits)

hetro_list = ['apple', 0, True]
print(hetro_list[0])
print(hetro_list[1])
print(hetro_list[-1])


# .append() リストの末尾に要素を追加する
fruits.append('grape')
print(fruits)

# .insert() リストの任意の位置に要素を追加する
fruits.insert(1, 'lemon')
print(fruits)

# .remove() リストから要素を削除する
fruits.remove('lemon')
print(fruits)

# .pop() リストから要素を削除する
fruits.pop(1)
print(fruits)

# .clear() リストから要素を全て削除する
fruits.clear()
print(fruits)

# .index() リストから要素を検索する
fruits = ['apple', 'orange', 'banana', 'peach']
print(fruits.index('banana'))

# .count() リスト内の要素の数をカウントする
fruits = ['apple', 'orange', 'banana', 'peach', 'banana']
print(fruits.count('banana'))
