N = int(input())
S = list(input())

# AokiかTakahashiか先に悪いカードを食べた方が負け
# 先手は高橋

# 偶数であれば高橋、奇数であれば青木の負け

for i in range(len(S)):
    if S[i] == '1':
        if i % 2 == 0:
            print('Takahashi')
            exit()
        elif i % 2 == 1:
            print('Aoki')
            exit()