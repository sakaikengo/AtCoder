# xとyの具材を入れると、(x+y) / 2の素材が出てくる

# 具材の価値として最大の値は?

# 2 <= N <= 50

#

N = int(input())

N_list = list(map(int, input().split()))

# 小さい順にソート

N_list.sort()

# print(N_list)

tmp = N_list[0]

for i in range(1, N):
    tmp = (tmp + N_list[i]) / 2

print(tmp)
