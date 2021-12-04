# i番目のすぬけくんが初めて宝石をもらう時刻は？

N = int(input())

S_list = list(map(int, input().split()))

T_list = list(map(int, input().split()))

# 時刻tに宝石をもらうとSi単位時間後、t+Siに（i+1）番目のすぬけくんに渡す

# すぬけくんは円周上に並んでいて反時計回りに1, 2, Nの番号

# 全部が最善を選び続ければそれが最善
ans_list = []
# 一番最初は高橋くんの一番目
ans_list.append(T_list[0])

tmp_time = 0

for i in range(0, N):
    # iが0の時
    T_list[0]
    # iが1の時
    T_list[0] + S_list[0]
    T_list[1]
    # iが2の時
    T_list[0] + S_list[0] + S_list[1]
    T_list[1] + S_list[0]
    T_list[2]
    
    for i in range(0, N):
        if i == 0:
            ans_list.append(T_list[i])
        else:
            # T_listの小さい方
            ans_list.append(min(,T_list[i]))


# 最後に高橋くんのリストと比較
for n in range(1, N):
    if ans_list[n] > T_list[n]:
        ans_list[n] = T_list[n]

for a in ans_list:
    print(a)