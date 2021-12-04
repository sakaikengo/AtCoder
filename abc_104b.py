#AcCepted

#文字列S
#①Sの先頭は大文字のA
#②Sの先頭から3文字目と末尾から2文字目の間に大文字のCがちょうど1文字含まれる
#③上記のA, Cを覗くすべての文字は小文字である

S = input()
S_list = list(S)
is_no = 0

#①
if S_list[0] != 'A':
    is_no = 1

#②
C_count = 0
for i in range(2, len(S) - 1):
    if S_list[i] == 'C':
        C_count += 1

if C_count != 1:
    is_no = 1

#③
lower_count = 0
for i in range(len(S)):
    if S_list[i].islower():
        lower_count += 1

if lower_count != len(S) - 2:
    is_no = 1

if is_no == 1:
    print('WA')
else:
    print('AC')