#Five Dishes

#1けた目が一番0以上で小さいものを最後に頼むと最少になる
#他のは繰り上げで10の位にする

import math

eat_list = [0] * 5

#標準入力から取得
for i in range(5):
    eat_list[i] = int(input())

print(eat_list)

max_min = 0
tmp_min = 0
#1のくらいで最大のものを求める
for i in range(5):
    tmp_min = 0
    tmp_min = eat_list[i] % 10
    if max_min <= tmp_min:
        max_min = tmp_min

for i in range(5):
    