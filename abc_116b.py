s = int(input())

# nが偶数ならn/2、nが奇数なら3n+1を繰り返す

#am = an(m > n)を満たすnが存在する

ans_count = 0


a = []

a.append(s)

for i in range(0, 10000000):
    if s % 2 == 0:
        s = s // 2
        ans_count += 1
        a.append(s)
    else:
        s = 3*s + 1
        ans_count += 1
        a.append(s)
    if s in a:
        a.remove(s)
        if s in a:
            print(ans_count+1)
            exit()
        else:
            a.append(s)