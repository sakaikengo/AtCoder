
S = input()

S_list = list(S)

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    if S_list[i] == 'x':
        num_list.remove(i)

print(num_list)

# 組み合わせを出力
ans = 0
for i in range(1, len(num_list)+1):
    ans *= i

print(i)

# 忘れてしまった組み合わせを出力

# 0000-9999までの10000通りを試す

#　'x'は使っていたら外す
# いったん別の配列を経由して判定

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10000):
    for j in range(4):
        d = 

    bool ok = True
    for i in range(i, 10):
        
