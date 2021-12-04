#Palindromic Numbers

#10000 <= A <= B <= 99999
#A以上B以下の整数のうち回文数となるものの個数はいくつか

ans_count = 0
num_list = [0]
str1 = ''


A, B = map(int, input().split())

#AからBまでループ
for i in range(A, B+1):
    #配列に格納
    str1 = str(i)
    num_list = list(str1)
    #indexが0番目と4番目と1番目と3番目が等しければans_countを+1する
    if num_list[0] == num_list[4] and num_list[1] == num_list[3]:
        ans_count += 1

print(ans_count)