T = int(input())
n_list = []
for _ in range(T):
    n_list.append(int(input()))
dp = [0] * (max(n_list)+1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(n_list)+1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for n in n_list:
    print(dp[n])
