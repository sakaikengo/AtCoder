N, X  = map(int, input().split())

#N個の商品を所持金X円で全て買うことができるか

money_sum = 0

product_list = list(map(int, input().split()))

for i in range(N):
    count = i + 1
    if count % 2 == 1:
        money_sum += product_list[i]
    else:
        money_sum += product_list[i] - 1

if money_sum <= X:
    print('Yes')
else:
    print('No')