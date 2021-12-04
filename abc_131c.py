import math

A, B, C, D = map(int, input().split())

# A以上B以下の整数のうち、CでもDでも割り切れないものの個数は?

# 1 <= A <= B <= 10**18
# 条件を満たすB以下の整数の個数からA-1以下の個数を引いたものが答え

C_multiple = B // C
D_multiple = B // D

# ↑を足したものから重複して引いたものを戻す(CとDの最小公倍数)
CandD_multiple = B // (C*D / math.gcd(C, D))

# A-1以下も同様に
AC_multiple = (A-1) // C
AD_multiple = (A-1) // D

ACandAD_multiple = (A-1) // (C*D / math.gcd(C, D))

print(int(B - C_multiple - D_multiple + CandD_multiple - ((A-1) - AC_multiple - AD_multiple + ACandAD_multiple)))
