# 8%の時A円、10%の時B円の消費税が課されるような商品の価格
# 条件が存在しなかったら-1を出力

A, B = map(int, input().split())

# 25 * 0.08 = 2
# 25 * 0.1 = 2 切り捨てで

# ans_a = A * 100 // 8

# ans_b_min = B * 10
# ans_b_max = (B+1) * 10 - 1
# # ans_bの最小範囲と最大範囲をとってans_aがその中に存在するならans_aを出力

# if ans_b_min <= ans_a <= ans_b_max:
#     print(ans_a)
# else:
#     print(-1)

# 1から10001まで繰り返す
for i in range(1, 10001):
        if i * 8 // 100 == A and i * 10 // 100 == B:
            print(i)
            exit()

print(-1)