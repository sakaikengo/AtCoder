
A, B, C = map(int, input().split())

# A以上B以下のCの倍数

for i in range(1, 1001):
    num = C * i
    if A <= num and num <= B:
        print(num)
        exit()
    if B < num:
        print(-1)
        exit()

print(-1)

