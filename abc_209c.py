#長さNの整数列C、条件を満たす整数列はいくつか
#条件
#1 <= Ai <= Ci(1 <= i <= N)
#Ai != Aj(1 <= i < j <= N)

N = int(input())

num_list = list(map(int, input().split()))

#Cが1, 3の場合答えは2
#Aが(1, 2)と(1, 3)の場合、(1, 1)は満たさない

#Cが3, 3, 4, 4の場合答えは12