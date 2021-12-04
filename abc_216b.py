N = int(input())

# 姓がSi、名がTi
# i < j かつ Si == Sj and Ti == Tj

ans_list = []

for i in range(N):
    last_name, first_name = input().split()
    full_name = last_name + '+' + first_name
    ans_list.append(full_name)

ans_set = set(ans_list)

if len(ans_set) == N:
    print('No')
else:
    print('Yes')
