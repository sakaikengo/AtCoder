N = int(input())

num_list = list(map(int, input().split()))

#1-Nまでの数を並び替えてnum_listと同じ配列を作ることができるか

list.sort(num_list)

correct_flg = 1
num = 0
for i in range(N):
    num += 1
    if num_list[i] != num:
        correct_flg = 0
        break
if correct_flg == 1:
    print('Yes')
else:
    print('No')
