P = int(input())

#P円の商品を最少で何枚の硬貨を使えば支払うことができるか

#1!=1
#2!=2
#3!=6
#4!=24
#5!=120

money = 1

money_list = []

for i in range(1, 20):
    money = money * i
    a = money
    money_list.append(a)

ans_count = 0

for i in reversed(range(1, len(money_list))):
    #配列の値がPより小さかったら割ってその値を答えに入れる
    if money_list[i] <= P:
        ans_count += P // money_list[i]
        P %= money_list[i]

if P == 1:
    print(ans_count + 1)
else:
    print(ans_count)


