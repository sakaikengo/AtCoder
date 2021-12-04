A, B, C = map(int, input().split())

# if pow(A, C) < pow(B, C):
#     print('<')
# elif pow(A, C) > pow(B, C):
#     print('>')
# elif pow(A, C) == pow(B, C):
#     print('=')

# AとBの大小と-かどうかを見ればいい
# Cが偶数の場合、-であろうと+になるので絶対値を比較
if C % 2 == 0:
    if abs(A) < abs(B):
        print('<')
    elif abs(A) > abs(B):
        print('>')
    elif abs(A) == abs(B):
        print('=')
# 奇数の場合
elif C % 2 == 1:
    # Aがマイナス、Bが正の場合
    if A < 0 and 0 <= B:
        print('<')
    elif A >= 0 and B < 0:
        print('>')
    elif A >= 0 and B >= 0:
        if abs(A) < abs(B):
            print('<')
        elif abs(A) > abs(B):
            print('>')
        elif abs(A) == abs(B):
            print('=')
    elif 0 > A and 0 > B:
        if abs(A) < abs(B):
            print('>')
        elif abs(A) > abs(B):
            print('<')
        elif abs(A) == abs(B):
            print('=')