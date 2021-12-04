
# 最初は花の高さは0

# 与えられる数列通りの高さにするには水やりを何回すればいいか

N = int(input())

height_list = list(map(int, input().split()))

ans = 0

# 初期値は全て0
first_list = [0] * N

# つながっているところが1以上なら同時に水やりできる

# 全て0になったら終了
# N回繰り返す
for i in range(N):
    # 最大でもとる値は100
    for j in range(100):
        # 0になったら次のループへ
        if height_list[i] == 0:
            break
        height_list[i] -= 1
        ans += 1
        # i以降で0のものがあるなら同時に水やりする
        for k in range(i+1, N):
            if not height_list[k] == 0:
                height_list[k] -= 1
            else:
                break

print(ans)