# 総数を求める公式
ans = N * (N-1) / 2

# 区間aからbの個数
# 区間[1, b]の個数-区間[1, a]の個数

# 最小公倍数
import math
math.lcm(A, B)

# 最大公約数
import math
math.gcd(A, B)

# N進数のnumから10進数のnumに変換
ten_N = int(str(num), N)

# エラトステネスの篩
prime_number_list = [i for i in range(10**5+1)]

# ループする限界値
root_X = 10**5 **0.5

# 時分秒
hour = N // 3600
minutes = N % 3600 // 60
seconds = N % 60

# 2の倍数を全て0に置き換える
for i in prime_number_list[3:]:
    if prime_number_list[i] % 2 == 0:
        prime_number_list[i] = 0

# 限界値まで↑の処理を繰り返す
for i in range(3, 10**5):
    if i > root_X:
        break
    if prime_number_list[i] != 0:
        for j in range(i, 10**5 + 1, 2):
            if i * j >= 10**5 + 1:
                break
            prime_number_list[i*j] = 0

prime_number_list2 = sorted(list(set(prime_number_list))[2:])
