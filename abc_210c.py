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
tmp_list = []

if N == K:
    color_set = set(color_list)
    print(len(color_set))
    exit()
else:
    for i in range(0, N-K, abs(K-N)):
        color_set = set(color_list[i:i+K])
        print(color_set)
        tmp_list.append(len(color_set))
        color_set.clear()

tmp_list.sort()
print(tmp_list)
ans_color = tmp_list[len(tmp_list)-1]
print(ans_color)