#Foods Loved by Everyone

#N人の人にM種類
N, M = map(int, input().split())

#最終的な答え
ans_count = 0
#調査の結果を格納
ans_list = [0] * M


for i in range(N):
    tmp_list = [0] * M
    tmp_list = list(map(int, input().split()))
    #list[0]の数だけ繰り返す
    for j in range(1, tmp_list[0] + 1):
        #好きだと答えた人の食べ物に関してカウントを+1する
        ans_list[tmp_list[j]-1] += 1


for k in range(M):
    if ans_list[k] == N:
        ans_count += 1

print(ans_count)