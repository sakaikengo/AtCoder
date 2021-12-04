N = input()

N_list = list(N)

ng_flg = 0

# def remove_list_zero(arr, value):
#     while value in arr:
#         arr.remove(value)

# remove_list_zero(N_list, '0')

# if len(N_list) % 2 == 0:
#     for i in range(len(N_list) // 2):
#         if not N_list[i] == N_list[len(N_list) - 1 - i]:
#             ng_flg = 1
# else:
#     for i in range(len(N_list) // 2):
#         if not N_list[i] == N_list[len(N_list) - 1 - i]:
#             ng_flg = 1

# if ng_flg == 1:
#     print('No')
# else:
#     print('Yes')

for i in range(10):
    S_tmp = '0' * i + N
    if S_tmp == S_tmp[::-1]:
        print('Yes')
        exit()

print('No')