# 753数7, 5, 3がそれぞれ1回以上現れこれら以外の数字は現れない
# 1以上N以下の753数は何個あるか

N = int(input())

ans = 0

# 7, 5, 3以外の数字が現れない

# 数nについて調べ、末尾に数字を追加した数を再起的に調べる関数
# use3, use5, use7はそれぞれ3, 5, 7を使用したかのフラグ
def dfs(n, use3, use5, use7):
    global ans
    if n > N:
        return
    if use3 and use5 and use7:
        ans += 1
    # 末尾に3, 5, 7をつけた数を再起的に調べる
    dfs(10*n+3, True, use5, use7)
    dfs(10*n+5, use3, True, use7)
    dfs(10*n+7, use3, use5, True)

# 何もない状態から呼び出す
dfs(0, False, False, False)

print(ans)
