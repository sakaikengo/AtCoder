A, B = map(int, input().split())

#A=100, B=600の場合
#下限は全て1の場合の100上限は全て6の場合の600

if A <= B and B <= A * 6:
    print('Yes')
else:
    print('No')