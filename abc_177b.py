#Substring

#2つの文字列S,T
#TがSの部分文字列となるようにSのいくつかの文字を書き換える。何文字書き換える必要があるか(最小)
#部分文字列=連続する文字列
#1 <= S, T <= 1000

S = input()
S_list = list(S)
T = input()
T_list = list(T)
#全てに当てはまらなかった場合の最大の値を設定(Tの長さ)
ans = len(T)

#何文字一致するかカウントしてS=Tなら0それ以外ならT-countを出力

#Sの
#全探索する、Sの長さからTの長さまで
for i in range(0, len(S) - len(T) + 1):
    #異なっているものをdiffでカウントする
    #ループごとにリセットする
    diff = 0
    #Tの長さループする
    for j in range(0, len(T)):
        #Tの文字列とSの文字列を比較して行って異なっていたらdiffを+1する
        if T_list[j] != S_list[i + j]:
            diff += 1
    #ループが終わるごとにansとdiffの少ない方をansに入れる
    ans = min(ans, diff)

print(ans)







