INF = 99999999 #일반적으로 9 여덟개
dp = [INF] * 50001
N = int(input())

dp[3] = 1
dp[5] = 1
# 맨 마지막으로 가져가는게 3kg냐 5kg냐로 일단 구분

for i in range(6, N+1):
    dp[i] = min(dp[i-3] + 1, dp[i-5] + 1, dp[i])

if dp[N] == INF:
    print(-1)
else:
    print(dp[N])
