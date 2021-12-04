#B-105

#1以上N以下の奇数で正の約数をちょうど8個もつものの個数
#1 <= N <= 200

N = int(input())
ans_count = 0

#iは1-105まで
for i in range(1, N):
    yakusuu_count = 0
    #jは1-105まで
    for j in range(1, i+1):
        if i % j == 0:
            yakusuu_count += 1
    print(yakusuu_count)
    if yakusuu_count == 8 and i % 2 == 1:
        ans_count += 1

print(ans_count)