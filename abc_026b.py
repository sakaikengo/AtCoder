#N重丸

#N重丸があり、外側から赤白交互に色を塗った時赤く塗られる部分の面積はいくつか？


#2で割れなかったら+、2で割れたら-

import math

N = int(input())

num = 0

num_list = []

for i in range(N):
    num_list.append(int(input()))

num_list.sort()

ans_sum = 0
if N % 2 == 1:
    for i in range(N):
        if i % 2 == 0:
            ans_sum += num_list[i] ** 2
        else:
            ans_sum -= num_list[i] ** 2
else:
    for i in range(N):
        if i % 2 == 1:
            ans_sum += num_list[i] ** 2
        else:
            ans_sum -= num_list[i] ** 2

print(ans_sum * math.pi)

