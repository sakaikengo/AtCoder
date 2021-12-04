#Small and Large Integers

#A以上B以下の整数の中で小さい方からK番目以内か大きい方からK番目以内である

A, B, K = map(int, input().split())

num_range = B - A

half_num = (A + B) / 2

if num_range < K or half_num < A + K:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, A+K):
        print(i)
    for j in range(B-K+1,B+1):
        print(j)