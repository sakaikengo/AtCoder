
# 条件を満たす0以上の整数が存在すればそのうち最少のものを出力、存在しなければ-1を出力

# 条件
# N桁、左から数えてsi桁目はciである

N, M = map(int, input().split())

# 答え

# 桁数カウント関数
def count_digit(num):
    return sum(c.isdigit() for c in str(num))

ans = [0] * N

num_list = []

for i in range(M):
    s = list(map(int, input().split()))
    num_list.append(s)

# num_listの[n][0]に番号、[n][1]に値が格納されている

for i in range(M):
    # num_list[i][0]-1といっちするものをansに入れていく
    # 入れるところが同じで値か0なら大丈夫
    if ans[num_list[i][0]-1] == num_list[i][1] or ans[num_list[i][0]-1] == 0:
        ans[num_list[i][0]-1] = num_list[i][1]
    else:
        print(-1)
        exit()

# 出力する
ans_int = ''.join(str(n) for n in ans)

ans_int = int(ans_int)
if N == count_digit(ans_int):
    print(ans_int)
else:
    print(-1)


