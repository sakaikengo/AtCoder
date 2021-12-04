N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort(reverse=True)
B_list.sort()

#Bリストの最小値からAリストの最大値を引く
ans = B_list[0] - A_list[0]

if ans < 0:
    print(0)
else:
    print(ans + 1)