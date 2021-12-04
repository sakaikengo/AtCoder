# 4つを頂点とし、全てのへんがx軸またはy軸に並行である長方形はいくつか？
import math

N = int(input())

point_x_list = []
point_y_list = []

for i in range(N):
    x, y = map(int, input().split())
    point_x_list.append(x)
    point_y_list.append(y)

# print(point_x_list)
# print(point_y_list)

# 4 <= N <= 2000
# 4重ループだと時間的にアウト
# 総数から満たさないものを引いていく?


ans_count = 0

# 2点が決まれば残りの2点が決まるので両方あれば+1
# 1つ目の頂点
for i in range(N):
    for j in range(i+1, N):
        count = 0
        difference1 = 0
        difference2 = 0
        real_diff = 0
        for k in range(j+1, N):
            difference1 = abs(point_x_list[i] - point_x_list[j])
            difference2 = abs(point_y_list[i] - point_y_list[j])
            # 差を求める
            real_diff = max(difference1, difference2)
            # 欲しい4つの点から残りの欲しい点2個を探す
            genten_x = min(point_x_list[i], point_x_list[j])
            genten_y = min(point_y_list[i], point_y_list[j])
            point1_x = genten_x + real_diff
            point1_y = genten_y
            point2_x = genten_x
            point2_y = genten_y + real_diff
            point3_x = genten_x + real_diff
            point3_y = genten_y + real_diff

            count_tmp = 0
            count_tmp2 = 3
            point_list = [[genten_x, genten_y], [point1_x, point1_y], [point2_x, point2_y], [point3_x, point3_y]]
            for l in range(4):
                if count_tmp == 2:
                    break
            if point_list[l][0] == point_x_list[i] and point_list[l][1] == point_y_list[i]:
                point_list[l][0] = -1
                point_list[l][1] = -1
                count_tmp += 1

            count_z = 0
            if point_list[0][0] == -1:
                point_list[0].remove(-1)
                count_z += 1
            if point_list[1-count_z][0] == -1:
                point_list[1-count_z].remove(-1)
                count_z += 1
            if point_list[2-count_z][0] == -1:
                point_list[2-count_z].remove(-1)
                count_z += 1
            if point_list[3-count_z][0] == -1:
                point_list[3-count_z].remove(-1)
                count_z += 1

            # 求める点を整理
            rest_point1_x = point_list[0][0]
            rest_point1_y = point_list[0][1]
            rest_point2_x = point_list[1][0]
            rest_point2_y = point_list[1][1]

            # 2点の差から残りの2点を求める
            # このループで最後まで行って残りの2点が存在したらplus
            if point_x_list[k] == rest_point1_x and point_y_list[k] == rest_point1_y:
                count += 1
            if point_x_list[k] == rest_point2_x and point_y_list[k] == rest_point2_y:
                count += 1
            if count == 2:
                ans_count += 1
                continue
print(ans_count)