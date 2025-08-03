N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

cnt = 0

for i in range(M):
    i, j = map(int, input().split())
    cnt = numbers[i-1]
    numbers[i-1] = numbers[j-1]
    numbers[j-1] = cnt

for i in range(N):
    print(numbers[i], end=' ')