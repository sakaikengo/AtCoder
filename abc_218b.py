
P_list = list(map(int, input().split()))

# 任意のiについてSのi文字目は辞書踏んで小さい方からPi番目の英小文字である

# アルファベットのa-zに対応している

a = 'abcdefghijklmnopqrstuvwxyz'
a_list = list(a)


for i in range(26):
    print(a_list[P_list[i]-1],end='')