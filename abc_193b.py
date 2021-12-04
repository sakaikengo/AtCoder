import math

#N軒の販売店

N = int(input())

#徒歩A分、販売価格P円、在庫X台

#0.5, 1.5, 2.5分後に在庫が1つずつ減少していく

#買うことができる場合の最少金額はいくらか、買えなかったら-1を出力

machine_list = [[0 for i in range(3)] for j in range(N)]

for i in range(N):
    a, p, x = map(int, input().split())
    machine_list[i][0] = a
    machine_list[i][1] = p
    machine_list[i][2] = x

#最少金額を格納する変数
min_money = 9999999999

#
for k in range(N):
    #もし1台以上残っていたら
    if 0 < machine_list[k][2] - machine_list[k][0]:
        if machine_list[k][1] <= min_money:
            min_money = machine_list[k][1]

#min_moneyが0のままなら-1を出力
if min_money == 9999999999:
    print(-1)
else:
    print(min_money)

