# i番目のすぬけくんが初めて宝石をもらう時刻は？

N = int(input())

S_list = list(map(int, input().split()))

T_list = list(map(int, input().split()))

# 時刻tに宝石をもらうとSi単位時間後、t+Siに（i+1）番目のすぬけくんに渡す

# すぬけくんは円周上に並んでいて反時計回りに1, 2, Nの番号

# 1番目は高橋くんから受け取ってスタートなので高橋くんの0番目を出力
# print(T_list[0])

# # N人が受け取るのでそれぞれが受け取るまでループ
# for i in range(1, N):
#     # 1つ前のすぬけくんからうけとるか、高橋くんからうけとるか早い方を出力
#     # つまり1つ前の高橋くん+1つ前のすぬけくんか現在の高橋くんか早い方
#     print(min(S_list[i-1] + T_list[i-1], T_list[i]))


# 全部が最善を選び続ければそれが最善
ans_list = []
# 一番最初は高橋くんの一番目
ans_list.append(T_list[0])

# 2番目はt+Siで横を見て行ってすべてans_listに格納
ans_list.append(S_list[0] + T_list[0])

sum = ans_list[1]

for s in range(2, N):
    sum += S_list[s-1]
    ans_list.append(sum)

# 2番目のT_listから始まった場合も同様に見ていく
k_sum_list = []
k_sum_list.append(T_list[0])
k_sum = 0
for k in range(1, N):
    k_sum = T_list[k]
    for l in range(k, N):
        k_sum += S_list[l]
        # 高橋くんリストの次の数を超えたら終了
        if l == N-1:
            k_sum_list.append(k_sum - S_list[l])
        elif T_list[k+1] < k_sum:
            k_sum_list.append(k_sum - S_list[l])

for n in range(1, N):
    if ans_list[n] > k_sum_list[n]:
        ans_list[n] = k_sum_list[n]

jk_list = []
jk_list.append(0)
for jk in range(1, N):
    jk_list.append(T_list[jk] + S_list[jk])

for jl in range(2, N):
    if ans_list[jl] > jk_list[jl-1]:
        ans_list[jl] = jk_list[jl-1]

# 最後にTたかはしくんのリストと比較して行って小さい方を格納
for i in range(1, N):
    if ans_list[i] > T_list[i]:
        ans_list[i] = T_list[i]

# 小さい方をリストに格納
min(, T_list[i])

# 結果を出力
for a in ans_list:
    print(a)