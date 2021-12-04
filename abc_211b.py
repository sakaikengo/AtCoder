S1 = input()
S2 = input()
S3 = input()
S4 = input()

tmp = ['H', '2B', '3B', 'HR']

if S1 in tmp:
    tmp.remove(S1)
else:
    print('No')
    exit()

if S2 in tmp:
    tmp.remove(S2)
else:
    print('No')
    exit()

if S3 in tmp:
    tmp.remove(S3)
else:
    print('No')
    exit()

if S4 in tmp:
    tmp.remove(S4)
else:
    print('No')
    exit()

if len(tmp) == 0:
    print('Yes')
