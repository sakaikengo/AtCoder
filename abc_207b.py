#全部A個、水色B個、赤色C

A, B, C, D = map(int, input().split())

#水色のボールの個数が赤色のボールの個数のD個以下になる最少操作は何回か

#操作、水色のボールB個と赤色のボールC個を容器に追加する

#最少操作回数を出力、無理なら-1を出力

#0回目
blue_ball = A
red_ball = 0

if B >= C * D:
    print(-1)
    exit()

for i in range(1, 10000000):
    #回数ごとにBとCが足されていく
    blue_ball += B
    red_ball += C
    if blue_ball <= red_ball * D:
        print(i)
        exit()