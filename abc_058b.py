# ∵∴∵

#Oは奇数番目
#Eは偶数番目

O = list(input())
E = list(input())

#答えを格納するリスト
ans_list = []
j = 0
#文字列の長さがOとEで等しい場合
for i in range(len(E)):
    ans_list.append(O[i])
    ans_list.append(E[i])

if len(O) == len(E):
    for i in ans_list:
        print(i, end='')
else:
    ans_list.append(O[len(O)-1])
    for i in ans_list:
        print(i, end='')