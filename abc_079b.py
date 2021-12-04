N = int(input())

Lucas = []

Lucas.append(2)
Lucas.append(1)

tmp = 0

for i in range(2, 86+1):
    tmp = Lucas[i-2] + Lucas[i-1]
    Lucas.append(tmp)

print(Lucas[N])