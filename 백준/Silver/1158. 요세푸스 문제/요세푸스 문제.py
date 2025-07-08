N, K = map(int, input().split())
table = []
for i in range(1, N+1):
    table.append(i)
res = []
index = 0
for i in range(N):
    index += K-1
    if index >= len(table):
        index = index % len(table)
    res.append(table.pop(index))
print('<', end='')
for i in range(N-1):
    print(res[i], end=', ')
print(res[N-1], end='>')