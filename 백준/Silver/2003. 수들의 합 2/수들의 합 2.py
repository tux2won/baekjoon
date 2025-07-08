N, M = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
count = 0

while (end < N):
    res = sum(arr[start:end+1])
    if res < M:
        end += 1
    elif res > M:
        start += 1
    else:
        count += 1
        end += 1

print(count)