# 高橋くんの給料

# 直属の部下がいない社員の給料は1

# 直属の部下がいる社員の給料はmax(その社員の直属の部下の給料) + min(その社員の直属の部下の給料) + 1

# 直属の部下が一人しかいない場合はその部下の給料の2倍+1が給料

#この時の高橋くんの給料は？

import sys
sys.setrecursionlimit(1000000)

N = int(input())

# child[i]:頂点iの子(部下)となる頂点たち
child = []

for i in range(N):
    child.append([])
for i in range(1, N):
    b = int(input())
    child[b-1].append(i)

# 再起関数を定義する

# dfs(i):頂点iの子の給料を全て求め、自身の給料を計算して返す
def dfs(i):
    # 子がいなければ1
    if len(child[i]) == 0:
        return 1
    else:
        values = []
        for j in child[i]:
            values.append(dfs(j))
        return max(values) + min(values) + 1

print(dfs(0))
