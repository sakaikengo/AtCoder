# 良い展望台がいくつあるか？

N, M = map(int, input().split())

height_list = list(map(int, input().split()))

# 通じる通路がある中で一番高ければOK

for i in range(M):
    num1, num2 = map(int, input().split())
    if height_list[num1-1]