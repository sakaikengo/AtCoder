
# 右隣のマスの高さが今いるマスの高さ以下である限り右隣のマスへ移動し続ける
# 最大で何回移動できるか

N = int(input())

space_list = list(map(int, input().split()))

# 1 <= N <= 10**5
# 1 <= Hi <= 10**9

# 累積和

max_count = 0

ans_list = []

count = 0

if N == 1:
    print(0)
    exit()

for i in range(N-1):
    if space_list[i] >= space_list[i+1]:
        count += 1
        ans_list.append(count)
    else:
        count = 0
        ans_list.append(count)

ans_list.sort(reverse=True)

print(ans_list[0])
