num = input()

num_list = list(num)

# 弱い暗証番号
# 4桁とも同じ数字、Xi+1がXiの次の数字(9の次は0)
# 弱い暗証番号ならWeak、強い暗証番号ならStrongを出力

num_set = set(num_list)

# 全桁一致の場合
if len(num_set) == 1:
    print('Weak')
    exit()

weak_count = 0

# 9でなくて+1したら次の数と等しくなる場合
if int(num_list[0]) != 9 and int(num_list[0]) + 1 == int(num_list[1]):
    weak_count += 1
elif int(num_list[0]) == 9 and int(num_list[1]) == 0:
    weak_count += 1

if int(num_list[1]) != 9 and int(num_list[1]) + 1 == int(num_list[2]):
    weak_count += 1
elif int(num_list[1]) == 9 and int(num_list[2]) == 0:
    weak_count += 1

if int(num_list[2]) != 9 and int(num_list[2]) + 1 == int(num_list[3]):
    weak_count += 1
elif int(num_list[2]) == 9 and int(num_list[3]) == 0:
    weak_count += 1

if weak_count == 3:
    print('Weak')
    exit()

print('Strong')