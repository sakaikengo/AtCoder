A, B, C = map(int, input().split())

num_list = [A, B, C]

list.sort(num_list, reverse=True)

print(num_list[0] + num_list[1])