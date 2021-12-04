N = int(input())

num_list = list(map(int, input().split()))

ans = 0

for i in range(N):
    if num_list[i] > 10:
        ans += num_list[i] - 10

print(ans)
