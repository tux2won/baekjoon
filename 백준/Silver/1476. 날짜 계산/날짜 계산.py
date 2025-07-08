arr = list(map(int, input().split()))
year = [0, 0, 0]
ans = 0
while not year == arr:
    year[0] += 1
    year[1] += 1
    year[2] += 1
    ans += 1
    if year[0] > 15:
        year[0] = 1
    if year[1] > 28:
        year[1] = 1
    if year[2] > 19:
        year[2] = 1
print(ans)