# N人全員が参加する集会を開く

# N人が消費する体力の総和としてありえる値の最小値はいくらか？

# 消費する体力は、座標pで集会を開く場合に(Xi - P) ** 2

N = int(input())

N_list = list(map(int, input().split()))

# 100通りなので全探索で全部の場合の消費する体力の総和を求める

tmp_ans = 0
ans = 10 ** 9

sorted_list = sorted(N_list)
H = sorted_list[N-1]

for i in range(H+1):
    tmp_ans = 0
    for j in range(N):
        tmp_ans += (N_list[j] - i) ** 2
    # 最小なら入れ替え
    if ans > tmp_ans:
        ans = tmp_ans
print(ans)