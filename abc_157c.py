
# 条件を満たす0以上の整数が存在すればそのうち最少のものを出力、存在しなければ-1を出力

# 条件
# N桁、左から数えてsi桁目はciである

N, M = map(int, input().split())

# 答え

# 桁数カウント関数
def count_digit(num):
    return sum(c.isdigit() for c in str(num))

# inputして配列に格納
c_list = []
s_list = []

for i in range(M):
    s, c = map(int, input().split())
    s_list.append(s)
    c_list.append(c)

# 0-999まで全探索して正解を求める
for i in range(1000):
    z = str(i)
    validate = True
    # 桁数がNと一致してなかったらcontinue
    if not len(z) == N:
        continue
    # 一致しているかの判定、cには何番目か・sには値が入ってる
    for j in range(M):
        # 条件を満たしていなかったらFalseを設定する
        if not z[s_list[j]-1] == str(c_list[j]):
            validate = False
    # 全て条件を満たしていたらreturn
    if validate == True:
        print(i)
        exit()

# 全て条件を満たしていなかったら-1を返却して終了
print(-1)
