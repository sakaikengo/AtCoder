# 整数Kの選び方は何通りか？

N = int(input())

# 難易度がK以上ならばARC
# 難易度がK未満ならばABC
# 上記が同じ数になるような整数Kの選び方は？

problem_list = list(map(int, input().split()))

# ソートして真ん中

problem_list.sort()

ans = problem_list[len(problem_list) // 2] - problem_list[len(problem_list) // 2 - 1]

print(ans)
