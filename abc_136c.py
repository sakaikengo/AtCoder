
N = int(input())

H_list = list(map(int, input().split()))

# マスの操作を行なって全部単調か右肩上がりにできるかどうか
# 操作：何もしないorマスの高さを1低くする

# 1 <= N <= 10**5

# 右のマスから高さが最大になるように調整していく

# N=1のときはYes
if N == 1:
    print('Yes')
    exit()

# N=5のときiは0-4
# 右から見ていく
for i in reversed(range(N-1)):
    # 条件を満たすなら次のループへ
    # 右の方が左以上
    if H_list[i] <= H_list[i+1]:
        continue
    # 1だけ小さいなら-1する
    elif H_list[i] - H_list[i+1] == 1:
        H_list[i] -= 1
        continue
    # それ以外ならNoを出力して終了
    else:
        print('No')
        exit()

print('Yes')