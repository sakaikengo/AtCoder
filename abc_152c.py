
# 1-Nの順列

N = int(input())

# 順列P1-PN
P_list = list(map(int, input().split()))

# 任意の整数j(1 <= j <=i)に対してPi <= Pj

# iより左側にiより小さい数値がいたらout

# 1 <= N <= 2 * 10**5

ans_count = 0

# 一番小さい値を持ってきてiと同じなら大丈夫

# tmp_list = []
# for i in range(N):
#     tmp_list = P_list[:i+1]
#     tmp_list.sort()
#     if tmp_list[0] == P_list[i]:
#         ans_count += 1

# print(ans_count)

# 最小値を保持して比較していく

min = 10**10

for i in range(N):
    if  P_list[i] < min:
        ans_count += 1
        min = P_list[i]

print(ans_count)