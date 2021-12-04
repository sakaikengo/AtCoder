#Stone Monument

#西側の塔から立っている高さが1, 1+2, 1+2+3


#a=雪に埋もれていない西の塔の高さ、b=雪に埋もれていない東の塔の高さ
a, b = map(int, input().split())

tower_height = 0


#for i in range(1, 1000):
#    tower_height += i
#    if a - tower_height < 0:
#        print(abs(a - tower_height))
#        exit()

#for i in range(1, 1000):
#    tower_height += i
#    if 1 <= tower_height - b:
#        print(tower_height - b)
#        exit()

#aとbは雪に埋もれていない部分

#aとbの塔の差を出力
tower_height_diff = b - a

for i in range(1, tower_height_diff):
    tower_height += i

print(tower_height - a)

#雪が何メートル積もっているか(地面から)

#50m積もっている場合は5, 16 差は11のため塔の高さはそれぞれ55, 66とわかる
