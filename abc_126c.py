
# 1-Nの整数が等確率で出るN面サイコロと表と裏が等確率で出るコイン

# 特点が1以上K-1以下である限りコインを振る、表が出たら2倍、裏が出たら特点が0になる

# 特点がK以上or0になったら終了、K以上なら勝ち、0なら負け

# 勝つ確率は?

N , K = map(int, input().split())

# 範囲
# 1 <= N <= 10**5
# 1 <= K <= 10**5

# 1-Nの出る確率

# 1の時に勝つ確率*2-Nを足していく

# ans = 0

# # 1の時に勝つ確率

# # 何倍すれば超えるか
# twice = 1
# tmp_ans = 1
# for i in range(1000000):
#     tmp_ans *= 2
#     if tmp_ans >= K:
#         break
#     twice += 1

# # Nのマス目で1が出る確率：1 / N
# first = (1 / N) * ((1 / 2) ** twice)

# print(ans_list)
# print(ans)
ans = 0
# サイコロを1回振り、1<= i <=Nが出る確率は、1/Nなのでそれぞれに対して求める
for i in range(1, N+1):
    # 1<= i <= Nの確率
    tmp = 1 / N
    # 今のi
    now = i
    # K以下なら繰り返すK以上になるまでループ
    while now < K:
        # 表が出たら2倍
        now *= 2
        # 1/2の**
        tmp /= 2
    # 足していく
    ans += tmp
print(ans)
