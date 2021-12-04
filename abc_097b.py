#Exponential

import math


X = int(input())

#X以下の最大のべき乗数はいくつか

exponential_list = []

ans = 0



for i in range(1, int(math.sqrt(X)) + 1):
    for j in range(2, int(math.sqrt(X)) + 1):
        exponential_list.append(i ** j)

exponential_list.sort()

ans_list = list(set(exponential_list))

for i in ans_list:
    if i <= X and ans < i:
        ans = i

if X == 1:
    print(1)
else:
    print(ans)