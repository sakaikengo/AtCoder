# 生徒たちの投稿した順番を復元

N = int(input())

N_list = list(map(int, input().split()))

# 計算量が多いためTLEになる
# for i in range(1, N+1):
#     for j in range(N):
#         if i == N_list[j]:
#             print(j+1, end=' ')
#             break

# 格納と同時に頭から番号を降っていき順番を並び替え番号を出力

ans_dict = {}

for i, num in enumerate(N_list):
    ans_dict[i] = num

# valueを昇順に並び替え、この時点でリストになる
ans_dict2 = sorted(ans_dict.items(), key=lambda x: x[1])

# keyの値に1をプラスして出力

for j, k in ans_dict2:
    print(int(j)+1, end=' ')