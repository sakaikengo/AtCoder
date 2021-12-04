C11, C12, C13 = map(int, input().split())
C21, C22, C23 = map(int, input().split())
C31, C32, C33 = map(int, input().split())

num_list = [[C11, C12, C13],[C21, C22, C23],[C31, C32, C33]]

#a1, a2, a3, b1, b2, b3の値が決まっていて、マス(i, j)にはai+ajが書かれている

#行差が全てb1-b2ならOK
if not num_list[0][0] - num_list[1][0] == num_list[0][1] - num_list[1][1] and num_list[0][1] - num_list[1][1] == num_list[0][2] - num_list[1][2]:
    print('No')
    exit()

if not num_list[1][0] - num_list[2][0] == num_list[1][1] - num_list[2][1] and num_list[1][1] - num_list[2][1] == num_list[1][2] - num_list[2][2]:
    print('No')
    exit()

#列差が全てa1-a2ならOK
if not num_list[0][0] - num_list[0][1] == num_list[1][0] - num_list[1][1] and num_list[1][0] - num_list[1][1] == num_list[2][0] - num_list[2][1]:
    print('No')
    exit()

if not num_list[0][1] - num_list[0][2] == num_list[1][1] - num_list[1][2] and num_list[1][1] - num_list[1][2] == num_list[2][1] - num_list[2][2]:
    print('No')
    exit()

print('Yes')