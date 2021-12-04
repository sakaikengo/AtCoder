# 4つを頂点とし、全てのへんがx軸またはy軸に並行である長方形はいくつか？

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
ans_count = 0
# 1つ目の頂点
for i in range(N):
    # 2つ目の頂点
    for j in range(i+1, N):
        # 3つ目の頂点
        for k in range(j+1, N):
            # 4つ目の頂点
            for l in range(k+1, N):
                    # AとBのx座標
                if not point_x_list[i] == point_x_list[j]:
                    continue
                # BとDのy座標
                if not point_y_list[j] == point_y_list[l]:
                    continue
                if not point_x_list[k] == point_x_list[l]:
                    continue
                if not point_y_list[k] == point_y_list[i]:
                    continue
                ans_count += 1

print(ans_count)