N = int(input())

score_list = list(map(int, input().split()))

sorted_list = sorted(score_list, reverse=True)

booby_award = sorted_list[1]

for i in range(N):
    if score_list[i] == booby_award:
        print(i + 1)
        exit()

