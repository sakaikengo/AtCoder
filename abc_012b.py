
N = int(input())

hour = N // 3600
if len(str(hour)) == 1:
    print('0' + str(hour) + ':', end='')
else:
    print(str(hour) + ':', end='')

minutes = N % 3600 // 60
if len(str(minutes)) == 1:
    print('0' + str(minutes) + ':', end='')
else:
    print(str(minutes) + ':', end='')

seconds = N % 60
if len(str(seconds)) == 1:
    print('0' + str(seconds), end='')
    print()
else:
    print(str(seconds), end='')
    print()