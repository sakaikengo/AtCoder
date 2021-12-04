N, A, B = map(int, input().split())

#一時的な合計
sum = 0

#対象の数字を格納
num = 0

#答えを格納
ans = 0

#1からNまでループ
for i in range(1, N+1):
    #各桁の和がA以上B以下か判定
    sum = 0
    num = i
    #1-4まででループ(4回)して余りを足していく(最大が36のため)
    for j in range(5):
        #1の位を足していく
        sum += num % 10
        #ループごとに
        num = num // 10
    #4桁(最大の場合)まで終わったら判定
    if A <= sum and sum <= B:
        #条件を満たしたらansに足していく
        ans += i
#合計を出力
print(ans)