N = int(input())

N_tax = int(N * 1.08)

if N_tax < 206:
    print('Yay!')
elif N_tax == 206:
    print('so-so')
else:
    print(':(')