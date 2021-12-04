# 最終的にたどり着く村の番号は？

N, K = map(int, input().split())

# K円を持った状態で村0にいる

# N人の友達がおりi人目の友達は村Aiにいて村AiについたときにBi円をもらう
# 1円を払うと次の村へいける
# 番号が同じものは金額を合計する
# 人がいなくなったら所持金額だけプラスして出力する


# N人の友達の位置と金額をリストに格納
friends_list = []
for i in range(N):
    A, B = map(int, input().split())
    friends_list.append([A, B])

# 村順にソート
friends_sorted_list = sorted(friends_list)
# print(friends_sorted_list)

# 村Mにたどり着くためにはM円必要
# 最大でもfriends_list[i][1]の合計の村までしか行けない




# for i in range(10**9):
#     # 次の村へいくごとに所持金を1減らす
#     K -= 1
#     for j,k in friends_sorted_list:
#         # 村が同じなら
#         if i+1 == j:
#             K += k
#             friends_sorted_list.remove(friends_sorted_list[j][0])
#     # 所持金が0になったら現在地を出力して終了
#     if K == 0:
#         print(i+1)
#         exit()