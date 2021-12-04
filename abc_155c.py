# 書かれた回数が最も多い文字列を全て、辞書順で小さい順に出力

import collections

N = int(input())

N_list = []

for i in range(N):
    a = input()
    N_list.append(a)

N_list_col = collections.Counter(N_list)

# print(N_list_col)

# 出現回数でsort

N_sorted = sorted(N_list_col.items(), reverse=True, key=lambda x: x[1])

# print(N_sorted)
# 最初（最大出現回数の値）を取得

tmp_list = []

for key, val in N_sorted:
    tmp_list.append(val)

max_count = tmp_list[0]

# print(tmp_list)

# 出現回数が最大のものをリストに格納
ans_list = []

for i, j in N_sorted:
    if j == max_count:
        ans_list.append(i)

# 辞書順でsort
ans_list.sort()

# 出力
for i in ans_list:
    print(i)