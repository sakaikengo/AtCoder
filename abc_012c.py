
kuku_sum = 2025

N = int(input())

kuku_ans = kuku_sum - N

# kuku_ansを求めることができる掛け算を出力する
for i in range(10):
    for j in range(10):
        if i * j == kuku_ans:
            print(str(i) + ' x ' + str(j))
