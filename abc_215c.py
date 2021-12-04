# 辞書順でソートして前からK番目に来るものはどれ？

import itertools

S, K = input().split()

S_list = list(S)

s_len = len(S)

# ソート
# S_list.sort()

ans_list = []

# 全ての組み合わせをセットに入れてソートしてK番目を出力

# for i in itertools.product(S):
#     ch = ''.join(i)
#     ans_list.append(ch)

for i in itertools.permutations(S, s_len):
    ch = ''.join(i)
    ans_list.append(ch)

# setに入れる
s = set(ans_list)
s_sorted = sorted(s)
# K番目を出力
y = list(s_sorted)
print(y[int(K)-1])