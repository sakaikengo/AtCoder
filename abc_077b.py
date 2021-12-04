#平方数

import math

N = int(input())

ans = 0


for i in reversed(range(N+1)):
    num = math.sqrt(i)
    if num.is_integer():
        print(i)
        exit()
