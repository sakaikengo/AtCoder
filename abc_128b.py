#Guidebook

#N個のレストランを紹介、S市にあり100点満点中P点
#市名が辞書順で早いものから紹介、同じ市に複数ある場合は点数が高いものから順に紹介

#N=レストランの数
N = int(input())

restraunt_list = [[0 for i in range(3)] for j in range(N)]

#標準入力から市と点数を取得

for i in range(N):
    restraunt_list[i] =  list(input().split())
    restraunt_list[i].append(i+1)

for j in range(N):
    restraunt_list[j][1] = int(restraunt_list[j][1])

#ソート処理 キーごとにソート、-をつけると昇順になる
li1 = sorted(restraunt_list, key=lambda x: (x[0], -x[1]))
li2 = sorted(restraunt_list, reverse=True, key=lambda x:x[1])

for m in range(N):
    print(li1[m][0])