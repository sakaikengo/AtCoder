
S1 = input()
S2 = input()
S3 = input()

S_list = list(input())

for i in range(len(S_list)):
    if int(S_list[i]) == 1:
        print(S1, end='')
    elif int(S_list[i]) == 2:
        print(S2, end='')
    elif int(S_list[i]) == 3:
        print(S3, end='')