#Smartphone Addiction

#バッテリー容量N, カフェを訪れる回数M, 帰宅する時刻T

N, M, T = map(int, input().split())
battery_max = N
is_ok = 1

#カフェにいる間はバッテリーが+、それ以外は-

#途中でバッテリーが0になったらNoを出力

battery_list = [[0 for i in range(2)] for j in range(M)]

for i in range(M):
    a, b = map(int ,input().split())
    battery_list[i][0] = a
    battery_list[i][1] = b

#最初のカフェに到着するまで
N -= battery_list[0][0]
if N <= 0:
    is_ok = 0

for i in range(M-1):
    cafe_stay = battery_list[i][1] - battery_list[i][0]
    N += cafe_stay
    if battery_max < N:
        N = battery_max
    not_cafe_stay = battery_list[i+1][0] - battery_list[i][1]
    N -= not_cafe_stay
    if N <= 0:
        is_ok = 0

#最後のカフェ滞在時間と最後にカフェをでてから家に到着するまで

N += battery_list[M-1][1] - battery_list[M-1][0]
if battery_max < N:
    N = battery_max
N -= T - battery_list[M-1][1]
if N <= 0:
    is_ok = 0


if is_ok == 1:
    print('Yes')
else:
    print('No')

