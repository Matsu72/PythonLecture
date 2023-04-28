# tuple:変更できないリスト
# 作成方法: ()で囲む
# 要素の取得: listと同じ
# 要素の変更: listと異なり、要素の変更はできない
# 要素の追加: listと異なり、要素の追加はできない
# 要素の削除: listと異なり、要素の削除はできない

data_of_birth = (1990, 1, 13)
print(data_of_birth[0])
print(data_of_birth[1])
print(data_of_birth[2])

# data_of_birth[0] = 1991 # TypeError: 'tuple' object does not support item assignment
# data_of_birth.append(1) # AttributeError: 'tuple' object has no attribute 'append'
# del data_of_birth[0] # TypeError: 'tuple' object doesn't support item deletion
year, month, date = data_of_birth
print(year)
print(month)
print(date)