import math

#1-9まで書かれた9K枚のカード

K = int(input())

#高橋くんに配られたカードの文字列S(5文字先頭4文字は1-9、末尾は裏向きのカード#)

S = input()

#青木くんに配られたカードの文字列T(5文字先頭4文字は1-9、末尾は裏向きのカード#)

T = input()

#高橋くんの勝つ確率はいくつか

#枚数が10^枚数になる

S_point = int(S[0:4])

T_point = int(T[0:4])

print(S_point)
print(T_point)

#1-9までが何枚あるかのリスト
takahashi_card_list = [1, 1, 1, 1, 1, 1, 1, 1, 1]
aoki_card_list = [1, 1, 1, 1, 1, 1, 1, 1, 1]

Takahashi_point = 0
Aoki_point = 0

Takahashi_point_sum = [0 for i in range(10)]
Aoki_point_sum = [0 for i in range(10)]

takahashi_card_list[int(S[0:1])] += 1
takahashi_card_list[int(S[1:2])] += 1
takahashi_card_list[int(S[2:3])] += 1
takahashi_card_list[int(S[3:4])] += 1

aoki_card_list[int(T[0:1])] += 1
aoki_card_list[int(T[1:2])] += 1
aoki_card_list[int(T[2:3])] += 1
aoki_card_list[int(T[3:4])] += 1

print(takahashi_card_list)
print(aoki_card_list)

#K枚以上のカードは取り除く
card_k = K + 2
card_list = [card_k, card_k, card_k, card_k, card_k, card_k, card_k, card_k, card_k]
print(card_list)

for j in range(9):
    card_list[j] -= takahashi_card_list[j]
    card_list[j] -= aoki_card_list[j]

print(card_list)

#2以上なら両方取得できるが1ならどっちかしか使えない
for i in range(9):
    takahashi_sum = 0
    #最後の#が1-9の場合の得点の合計を考える
    for j in range(9):
        #card_listの残りが0の場合=全て使用している場合はスキップする
        if card_list[j] != 0:
            break
            takahashi_card_list[j] += 1
        if takahashi_card_list[j] == 1:
            takahashi_card_list[j] -= 1
        else:
            #枚数分10の何乗かをする
            takahashi_sum += j * (10 ** (takahashi_card_list[i]-1))
            takahashi_card_list[j] -= 1
    #iが終了した時の合計をリストに追加
    Takahashi_point_sum[i] = takahashi_sum



#aokiとtakahashiのpoint_listを突き合わせてtakahashiの勝つ確率を計算する

ans_count = 0
for i in range(10):
    if Aoki_point_sum[i] < Takahashi_point_sum[i]:
        ans_count += 1

print(ans_count / 9)