num = input()

if len(num) == 4:
    x = num[0:2]
    y = num[3:4]
else:
    x = num[0:1]
    y = num[2:3]

if int(y) <= 2:
    print(x+'-')
elif int(y) <= 6:
    print(x)
else:
    print(x+'+')

