N = int(input())

N_list = list(map(int, input().split()))

# i-jの絶対値が200の倍数の個数は？

ans = 0

# Aiを200で割った余りとAjを200で割った余りが一致する
# 0から199の間に収まる
# ↓
# Ai - Aj == 0 → Ai == Aj

# 個数(1-199がそれぞれ何個存在するか)を記録しておく

# nC2を足して出力
# list[i] * list[i]-1 / 2

ans_list = [0] * 200

for i in range(N):
    n_mod = N_list[i] % 200
    ans_list[n_mod] += 1

# print(ans_list)

ans = 0

for j in range(200):
    ans += (ans_list[j] * (ans_list[j]-1)) // 2

print(ans)