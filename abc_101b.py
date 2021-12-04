#Digit Sums

#NがS(N)で割り切れるかどうか

N = int(input())

N_list = list(str(N))

S = 0
for i in range(len(N_list)):
    S += int(N_list[i])


if N % S == 0:
    print('Yes')
else:
    print('No')