S = input()

#配列の後ろから出力
#6なら9、9なら6を出力

S_list = list(S)

for i in reversed(range(0, len(S))):
    if S_list[i] == '6':
        print('9', end='')
    elif S_list[i] == '9':
        print('6', end='')
    else:
        print(S_list[i], end='')