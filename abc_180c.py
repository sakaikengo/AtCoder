# N個のシュークリームを分割することなく平等に分けることができる人数

import math

N = int(input())

# Nの約数を全て出力

def divisor_list(num):
    divisors = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i ** 2 == num:
                continue
            divisors.append(num // i)
    return sorted(divisors)

num_list = divisor_list(N)
for i in num_list:
    print(i)