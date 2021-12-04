
N = int(input())

A_list = list(map(int, input().split()))

B_list = list(map(int, input().split()))

# N人の勇者が協力して最大何体のモンスターを倒すことができるか

# i番目の勇者はiまたはi+1番目のモンスターをBi体まで倒すことができる

ans = 0

for i in range(N):
    # i番目のモンスターを倒し切れる場合
    if A_list[i] <= B_list[i]:
        ans += A_list[i]
        B_list[i] -= A_list[i]
        A_list[i] = 0
        # i+1番目のモンスターもi番目の勇者が倒し切れる場合
        if A_list[i+1] <= B_list[i]:
            ans += A_list[i+1]
            A_list[i+1] = 0
        # 倒しきれなかった場合
        else:
            A_list[i+1] -= B_list[i]
            ans += B_list[i]
    # 倒しきれなかった場合
    else:
        ans += B_list[i]

print(ans)