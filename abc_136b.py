#Uneven Numbers

#N以下の正の整数のうち桁数が奇数であるものはいくつか
#1<= N <= 100000


N = int(input())

#1-9,100-999,10000-99999
#101の場合は1-9+2

#1-9の場合
if N < 10:
    print(N)
#10-99の場合
elif N < 100:
    print(9)
#100-999の場合
elif N < 1000:
    print(N - 90)
#1000-9999の場合
elif N < 10000:
    print(909)
#10000-99999の場合
elif N < 100000:
    print(N - 9999 + 909)
#100000の場合(上限値)
else:
    print(90909)

#公式回答
#文字列に変換して長さを数える
#1からN+1までループをして長さを2で割ってあまりが1なら長さが奇数となるのでans_countを+1する