
# xをxとKの差の絶対値で置き換える
# 上記の操作を0回以上行った時にとりうるNの最小値は？

N, K = map(int, input().split())

# Kが1の場合は0

t = N % K

x = K - t

print(min(t, x))