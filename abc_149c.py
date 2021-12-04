
# X以上の素数のうち最少のものを求めよ

X = int(input())

# 2-10**5までの素数のリストを作成する

prime_number_list = [i for i in range(10**5+1)]

# ループする限界値
root_X = 10**5 **0.5

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

# for文でX以上のものを出力
for i in range(len(prime_number_list2)):
    if prime_number_list2[i] >= X:
        print(prime_number_list2[i])
        exit()
print(100003)