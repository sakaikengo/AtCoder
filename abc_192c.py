
# g1(x) = xを十進法で表した時の各桁の数字を大きい順に並び替えてできる整数
# g2(x) = xを十進法で表した時の各桁の数字を小さい順に並び替えてできる整数
# f(x) = g1(x) - g2(x)

# N,Kが与えられるのでakを求める

N, K = map(int, input().split())

ans_list = []

ans_list.append(N)


# Kまで再帰的に求めていく
for i in range(1, K+1):
    # 昇順にソート
    tmp_list = []
    tmp_list = list(str(ans_list[i-1]))
    min_list = sorted(tmp_list)
    max_list = sorted(tmp_list, reverse=True)
    # 結合して数値に戻す
    min = int(''.join(min_list))
    max = int(''.join(max_list))
    ans_list.append(max - min)

# ans_listのKを出力
print(ans_list[K])