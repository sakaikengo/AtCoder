
# 120回以内の魔法で箱の中のボールをちょうどN個

N = int(input())

# A:箱の中にボールを1つ増やす
# B:箱の中のボールを2倍にする

# 出力はA,Bからなる文字列

# 1 <= N <= 10**18

# 偶数ならB、奇数ならAを格納して0になったら逆に出力

ans_list = []

while N != 0:
    if N % 2 == 0:
        ans_list.append('B')
        N = N // 2
    else:
        ans_list.append('A')
        N -= 1

for i in range(len(ans_list)):
    print(ans_list[len(ans_list)-1-i], end='')