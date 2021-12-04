# Xとの差の絶対値が一番小さいものを求める

import math

X, N = map(int, input().split())

if N != 0:
    num_list = list(map(int, input().split()))
else:
    print(X)
    exit()

# forで前と後ろを調べて行ってnum_listを含まない絶対値を比較、一緒なら小さい方

before_num = 0
after_num = 0

# 現在値から100までで一番小さいもの
for i in range(X, 102):
    if i not in num_list:
        # print(i)
        after_num = i
        break
    else:
        after_num = i

# 現在地から0までで一番小さいもの
for j in reversed(range(0, X+1)):
    # print(j)
    if j not in num_list:
        before_num = j
        break
    else:
        before_num = 0

if after_num == before_num:
    print(X)
elif abs(X - after_num) == abs(X - before_num):
    print(before_num)
elif abs(X - after_num) > abs(X - before_num):
    print(before_num)
elif abs(X - after_num) < abs(X - before_num):
    print(after_num)

# print(after_num)
# print(before_num)
