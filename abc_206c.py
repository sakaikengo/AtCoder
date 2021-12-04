

N = int(input())

num_list = list(map(int, input().split()))

# i <= jを満たす整数の組の合計を求める
# Ai != Aj

sorted_list = sorted(num_list)

# 重複している数字の分をそれ以外の数にかければ良い
# それを足していく

ans = 0

# ループして同じ数だけ引いて0になったら終了
# 残りの数をansに足していく

# for i in range(N):
#     # 対象の数字
#     counta = sorted_list.count(sorted_list[i])
#     if counta == 1:
#         ans += len(sorted_list)-1
#         sorted_list.remove(sorted_list[i])
#     else:
#         ans += counta * (len(sorted_list) - counta)
#         if sorted_list[i] in sorted_list:
#             sorted_list.remove(sorted_list[i])
#     if len(sorted_list) == 0:
#         exit()
# print(ans)

# setに入れてNをかけていく
# 同じ数がある分それを掛け算する

import collections

list_count = collections.Counter(sorted_list)

# keyを取得
list_keys = list_count.keys()
# print(list_keys)

list_values = list(list_count.values())

# for i in range(len(list_values)):
#     # その数*残りリストの合計
#     ans += list_values[i] * sum(list_values[:i])

# print(ans)

# Aが同じi,jを探して全体からこれを引く
# 総数の公式は n * (n-1)/2
ans = N*(N-1) / 2
for i in range(len(list_values)):
    # 重複するのも総数を求める
    ans -= list_values[i]*(list_values[i]-1)/ 2

print(int(ans))