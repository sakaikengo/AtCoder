# 1以上M以下の整数Kを全て求める

import math

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

# 1行目に出力する整数の数xを出力、続いて小さい方から順に1行に1つずつ

# gcd(Ai, k) = 1となる

counter = 0

ans_list = []

m_list = []

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# num_listからMの約数を削除する

m_list_tmp = make_divisors(M)



for i in range(M):
    m_list.append(i)

for i in range(1, len(m_list_tmp)):
    if m_list_tmp[i] in m_list:
        m_list.remove(m_list_tmp[i])

ans_list = []

# TLEになる
for i in range(1, len(m_list)):
    counter = 0
    for j in range(len(num_list)):
        if math.gcd(num_list[j], m_list[i]) == 1:
            counter += 1
        else:
            continue
    if counter == len(num_list):
        ans_list.append(m_list[i])

# ans_listの長さを出力
print(len(ans_list))

# ans_listの要素を順にソートして出力
for k in ans_list:
    print(k)
