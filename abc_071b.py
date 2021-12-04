#Not Found

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

S = input()

S_list = list(S)
ans_list = []
ans_count = 26
for i in range(len(S)):
    for j in range(len(alpha_list)):
        if S_list[i] == alpha_list[j]:
            alpha_list[j] = 0
            continue

for k in range(len(alpha_list)):
    if alpha_list[k] != 0:
        ans_list.append(alpha_list[k])
        ans_count += 1
    ans_count -= 1

if ans_count == 0:
    print('None')
else:
    print(ans_list[0])