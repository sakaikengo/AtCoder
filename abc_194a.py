#標準入力から読み取り
#a=無脂乳固形分, b=乳脂肪分
a, b = map(int, input().split())

milk_solids = a + b

if 15 <= milk_solids and 8 <= b:
    print(1)
elif 10 <= milk_solids and 3 <= b:
    print(2)
elif 3 <= milk_solids:
    print(3)
else:
    print(4)