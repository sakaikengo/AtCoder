import math

#整数Nが与えられる

#1以上N以下の整数のうち2以上の整数a, bを用いてa^bと表せないものはいくつあるか

ok_count = 0

N = int(input())

ok_list = set()
N_limit = int(math.sqrt(N)) + 3

for i in range(2, N_limit):
    for j in range(2, N_limit):
        num = i ** j
        if num <= N:
            ok_list.add(num)
        if N <= num:
            break

#set()で重複を削除
print(N - len(ok_list))