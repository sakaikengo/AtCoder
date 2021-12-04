N = int(input())

num_list = list(map(int, input().split()))

# 全て偶数である時黒板に書かれている整数全てを2で割ったものに置き換える

# 1 <= N <= 200

ans = 0

while True:
    for i in range(N):
        if num_list[i] % 2 == 1:
            print(ans)
            exit()
        else:
            num_list[i] = num_list[i] // 2
    ans += 1

print(ans)