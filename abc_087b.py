A = int(input())
B = int(input())
C = int(input())
X = int(input())

# 500円A枚、100円B枚、50円C枚で合計金額をX円にする方法は何通りあるか

# A=5B, B=2C, A=10C

ans = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i * 500 + j * 100 + k * 50 == X:
                ans += 1

print(ans)
