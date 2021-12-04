#完全二分木の形のトーナメント
#準優勝するのはだれか
#レート(番号)の大きい方が勝つ

#トーナメントN人の対戦回数はN-1回
N = int(input())

tournament_list = list(map(int, input().split()))

#最終的なサイズが2になるまで繰り返し
while(tournament_list.size() > 2):
    int[] na
    for i in range(tournament_list.size()):
        i += 1
        