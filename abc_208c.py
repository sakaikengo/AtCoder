#N人の国民、K個のお菓子

N, K = map(int, input().split())

national_list = list(map(int, input().split()))

#N個以上なら全員に1個配る
#N個以下なら国民番号が少ない順に1配る

#全員に配る数
sweets_num = K // N
remainder = K % N

# 残りをループで若い順から配る

d = {}

for i, num in enumerate(national_list):
    d[i] = num

print(d)