#2番目に高い山の名前

N = int(input())

ans = ''
tmp_height = 0
dict = {}

for i in range(N):
    name, height = input().split()
    dict[name] = int(height)

dict_sorted = sorted(dict.items(), key=lambda x:x[1])

ans_dict = dict_sorted[N-2]

print(ans_dict[0])

