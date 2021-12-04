#N人の従業員
N = int(input())

#仕事Aと仕事Bでそれぞれ求める
#仕事Aの時間と仕事Bにかかる時間が入力される

n_time_min = 10000000
a_job_time = [[0] for i in range(N)]
b_job_time = [[0] for i in range(N)]


#N人分繰り返す
for i in range(N):
    a_time, b_time = map(int, input().split())
    a_job_time[i] = a_time
    b_job_time[i] = b_time

ans = 10000000

for i in range(N):
    for j in range(N):
        ans = min(ans, a_job_time[i] + b_job_time[j] if i == j else max(a_job_time[i], b_job_time[j]))
print(ans)
