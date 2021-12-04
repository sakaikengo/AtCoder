N, K = map(int, input().split())

color_list = list(map(int, input().split()))

# 連続して並んでいるK個のキャンディがもらえる
# 色の種類の最大値を出力

# 連続しない長さの最大を求めれば大丈夫

ans_color = 0

# 開始位置

# ループが終わったら最大値を出力

# setに入れてKの範囲の重複のないものが何個かを見る、それの最大値はいくつか

color_set = set()

if N == K:
    for i in range(K):
        color_set.add(color_list[i])
    ans_color = len(color_set)
else:
    for i in range(0, N-K, K-N):
        for j in range(K):
            color_set.add(color_list[i+j])
        if ans_color < len(color_set):
            ans_color = len(color_set)
        color_set.clear()

print(ans_color)