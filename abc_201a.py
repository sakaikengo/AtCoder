A1, A2, A3 = map(int, input().split())

num_list = [A1, A2, A3]

list.sort(num_list)

if num_list[2] - num_list[1] == num_list[1] - num_list[0]:
    print('Yes')
else:
    print('No')