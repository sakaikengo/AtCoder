#String Rotation

#文字列Sを回転して文字列Tに一致させられるか

S = input()

T = input()

#SとTの文字が一致していればok

S_list = list(S)

T_list = list(T)

S_list.sort()

T_list.sort()

ans_count = 0

for i in range(len(S)):
    if S_list[i] == T_list[i]:
        ans_count += 1

if ans_count == len(S):
    print('Yes')
else:
    print('No')