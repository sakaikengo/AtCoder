import math

Y = input()
X = list(Y)

if isinstance(Y, int) == True:
    print(Y)
else:
    for i in range(len(X)):
        if X[i] != '.':
            print(X[i], end='')
        elif X[i] == '.':
            break
