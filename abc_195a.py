#m = 魔法が聞くかどうか, h=モンスターの体力

m, h = map(int, input().split())

if h % m == 0:
    print('Yes')
else:
    print('No')