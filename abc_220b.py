
K = int(input())
A, B  = map(int, input().split())

# A*BをK進数から10進数に直して計算→出力

ten_A = int(str(A), K)

ten_B = int(str(B), K)

print(ten_A * ten_B)