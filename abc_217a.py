S, T = input().split()

ST_list = [S, T]

ST_list.sort()

if ST_list[0] == S:
    print('Yes')
else:
    print('No')