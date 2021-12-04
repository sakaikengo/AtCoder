# 1以上M以下の整数Kを全て求める

import math

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

# 1行目に出力する整数の数xを出力、続いて小さい方から順に1行に1つずつ

# gcd(Ai, k) = 1となる

counter = 0

ans_list = []

# TLEになる
for i in range(1, M+1):
    counter = 0
    for j in range(N):
        if math.gcd(num_list[j], i) == 1:
            counter += 1
        else:
            continue
    if counter == N:
        ans_list.append(i)

# ans_listの長さを出力
print(len(ans_list))

# ans_listの要素を順にソートして出力
for k in ans_list:
    print(k)
