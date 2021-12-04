# 迷路を解く最少移動手数を求める

from collections import deque

R, C = map(int, input().split())

start_y, start_x = map(int, input().split())

goal_y, goal_x = map(int, input().split())

S = []

for i in range(R):
    s = input()
    S.append(s)

# スタート、ゴールの座標を0始まりに直す
start_y -= 1
start_x -= 1
goal_y -= 1
goal_x -= 1

# 最少移動回数を管理する二次元配列、-1なら未訪問
dist = []
for j in range(R):
    dist.append([-1]*C)

# キューを用意
Q = deque()
Q.append([start_y, start_x])
# 始点を入れる
dist[start_y][start_x] = 0

# キューから取り出しながら探索
while len(Q) > 0:
    i, j = Q.popleft()
    # 4つの隣マスを確認
    for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        # 盤面の範囲内でなければスルー
        if not (0 <= i2 < R and 0 <= j2 < C):
            continue
        # 壁マスであれば無視
        if S[i][j] == '#':
            continue
        # もし未訪問(dist[i2][j2]が-1)であれば距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

# 視点から終点までの最少移動回数を出力
print(dist[goal_y][goal_x])