

alp_list = list(input())

N = int(input())

# alp_listのアルファベット順に並べ替える

name_list = []

# いったん数字に変換
for i in range(N):
    name = list(input())
    tmp_list = []
    name_num = ''
    for j in range(len(name)):
        for k in range(len(alp_list)):
            if name[j] == alp_list[k]:
                tmp_list.append(int(k))
                break
    # print(tmp_list)
    name_list.append(tmp_list)

# print(name_list)

# for i in range(N)

# sort
# sorted_list = sorted(name_list, key=int)

sorted_list = sorted(name_list, )

# その後アルファベットに再変換して出力
# print(sorted_list)

ans_list = []

# print(sorted_list)

for i in range(N):
    name = list(sorted_list[i])
    tmp_list = []
    # 数字からアルファベットに戻す
    for j in range(len(name)):
                tmp_list.append(alp_list[int(name[j])])
                # print(tmp_list)
    ans_alp = ''.join(tmp_list)
    ans_list.append(str(ans_alp))

for i in ans_list:
    print(i)