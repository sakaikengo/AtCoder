N = int(input())

num_list = list(map(int, input().split()))

#10**18を超える場合は-1を出力

ans = 1

#0が含まれていたら0を出力
if 0 in num_list:
    ans = 0
else:
    for num in num_list:
        ans *= num
        if ans > 1000000000000000000:
            ans = -1
            break

print(ans)
