N, K = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    for k in range(1, K + 1):
        ans += i*100 + k

print(ans)
