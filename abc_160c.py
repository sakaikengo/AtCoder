# 1周Kメートルの円形の湖、その周りにN軒の家

# i番目の家は北端から時計回りにAiメートルの位置

# いずれかの家から出発してN軒すべての家を訪ねるための最短移動距離はいくつか？

K, N = map(int, input().split())

house_list = list(map(int, input().split()))

# 始点を通らないためループの前に計算
distance_1_to_N = house_list[N-1] - house_list[0]

ans_list = []

for i in range(1, N):
    # 湖の始点から対象の家までの距離
    a = K - house_list[i]
    # 湖の始点から対象から１個前の家までの距離
    b = house_list[i - 1]
    ans_list.append(a + b)

# 一番距離の短いものを出力
ans_list.sort()
print(min(ans_list[0], distance_1_to_N))