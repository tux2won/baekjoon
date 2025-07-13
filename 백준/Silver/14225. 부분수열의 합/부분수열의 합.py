from itertools import combinations
N = int(input())
S = list(map(int, input().split()))
ans = set()
for i in range(1, len(S)+1):
    for comb in combinations(S, i):
        sum_value = sum(comb)
        ans.add(sum_value)
missing_sum = 1
while True:
    if missing_sum not in ans:
        print(missing_sum)
        break
    missing_sum += 1