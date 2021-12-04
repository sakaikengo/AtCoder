#Billiards

#現在の位置(x_start, y_goal), 最終的な座標(x_start, y_goal)
x_start, y_start, x_goal, y_goal = map(int, input().split())

#狙う座標(x_point, 0)、x_pointはいくつか？

#y座標の変化量を考えるとy_start:y_goalで内分する点でx軸と交わる
#このため内分する座標を求める
#x_startからx_goalへの変化を(x_start*y_goal+x_goal*x_start)/(y_start+y_goal)で求めることができる

print((x_start * y_goal + x_goal * y_start) / (y_start + y_goal))