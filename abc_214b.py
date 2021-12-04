
# a+b+c <= S and a * b * c <= Tをみたす整数の組みはいくつか？

S, T = map(int, input().split())

ans = 0

# Sの条件を満たすもの
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i + j + k <= S and i * j * k <= T:
                ans+=1

print(ans)