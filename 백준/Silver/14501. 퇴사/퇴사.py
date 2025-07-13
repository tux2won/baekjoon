N = int(input())
T_list = []
P_list = []
ans_list = []
for _ in range(N):
    T, P = map(int, input().split())
    T_list.append(T)
    P_list.append(P)

max_value = 0
dp = [0] * (N+1)
 

for i in range(N-1, -1, -1):
    time = T_list[i] + i # 7, 5
    if time <= N:
        dp[i] = max(P_list[i]+ dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)