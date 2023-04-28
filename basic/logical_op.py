# 論理演算子（logical operators）
# 論理演算子は、複数の条件を組み合わせるために使用する演算子です。
# 論理演算子には、and、or、notの3つがあります。
# and
# andは、左右の条件が両方ともTrueの場合にTrueを返します。
# 以下の例では、aが5より大きく、かつ、aが10より小さい場合にTrueを返します。
a = 7
print(a > 5 and a < 10)  # True

# or
# orは、左右の条件のどちらかがTrueの場合にTrueを返します。
# 以下の例では、aが5より大きい、または、aが10より小さい場合にTrueを返します。
a = 7
print(a > 5 or a < 10)  # True

age = 13
height = 140
print(age > 10 and height > 110)  

master = False
job_experience = 5
print(master or job_experience >= 5)
