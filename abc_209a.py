A, B = map(int, input().split())

if A == B:
    print(1)
elif A < B:
    print(B - A + 1)
elif B < A:
    print(0)