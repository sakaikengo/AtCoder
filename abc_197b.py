height, width, x, y = map(int, input().split())

#同じ行or同じ列で#でないもの

MAX_ANS = height + width - 1

#答えを格納
#(x, y)は'#'ではないため初期値は1

ans = 1

#標準入力から取得
squares_list = [list(input()) for i in range(height)]

#print(squares_list)

#(x,y)からみて見えるマスはいくつか

#(x,y)から左方向
for i in reversed(range(0, y-1)):
    if squares_list[x-1][i] =='.':
        ans += 1
    elif squares_list[x-1][i] == '#':
        break

#(x,y)から右方向
#iは0-4まで繰り返し
for i in range(y, width):
    if squares_list[x-1][i] =='.':
        ans += 1
    elif squares_list[x-1][i] == '#':
        break

#(x,y)から上方向
#(1,4)
#squares_list[0][3]
for i in reversed(range(0, x-1)):
    if squares_list[i][y-1] == '.':
        ans += 1
    elif squares_list[i][y-1] == '#':
        break

#(x,y)から下方向
for i in range(x, height):
    if squares_list[i][y-1] == '.':
        ans += 1
    elif squares_list[i][y-1] == '#':
        break

print(ans)

