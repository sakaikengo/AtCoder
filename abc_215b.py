N = int(input())

# 2 ** k <= Nとなる最大の整数k

num = 2

for i in range(1, 100):
    num = 2 ** i
    if num > N:
        print(i-1)
        exit()
