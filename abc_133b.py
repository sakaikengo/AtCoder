#Good Distance

#D次元空間上にN個の点がある

import math

N, D = map(int, input().split())

#i番目の点の座標は(xi1, xi2, ..., xiD)
#座標(y1, y2, yD)と座標(z1, z2, zD)の点の距離は√(y1-z1)^2 + (y2-z2)^2+ ... +(yD-zD)^2
#i番目とj番目の点の距離が整数となる組はいくつあるか

point_list = [[0 for i in range(D)] for i in range(N)]

#標準入力から座標を読み込み
#1 2
#5 5
#-2 8
#[[1, 2], [5, 5], [-2, 8]]
#point_list[2][3]
for i in range(N):
    point_list[i] = list(map(int, input().split()))

#答えを格納する変数
ans_count = 0
#距離を保存する変数
distance1 = 0
#ループで距離を求める
#0, 1, 2で3回ループ
for j in range(N):
    #lはjからNまでループ
    for l in range(j+1 , N):
        distance1 = 0
        #D回ループ
        for k in range(D):
            distance1 += abs(point_list[l][k] - point_list[j][k]) ** 2
        if math.sqrt(distance1).is_integer():
            ans_count += 1

print(ans_count)