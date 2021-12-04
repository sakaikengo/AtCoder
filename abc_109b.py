#Shiritori

#Noflg
is_no = 0
N = int(input())

word_list = [''] * N

for i in range(N):
    word_list[i] = input()

#まだ発言していない単語である
#先頭の文字は直前に発言した単語の末尾の文字と一致する
#同じ単語が存在したらNoflgを1に設定
for i in range(N):
    for j in range(i+1, N):
        if word_list[i] == word_list[j]:
            is_no = 1

#一番最初の単語の最後の文字から一番最後の単語のの最初の文字が一致しているかを判定
for k in range(N-1):
    if word_list[k][-1:] == word_list[k+1][0:1]:
        continue
    else:
        is_no = 1




if is_no == 1:
    print('No')
else:
    print('Yes')
