import copy
import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한을 늘림

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
count = 0

min_rain = 1
# min_rain = min(min(row) for row in map)
max_rain = max(max(row) for row in map)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(m, x, y, r):
    global count
    if x<0 or y<0 or x>=N or y>=N:
        return
    if m[x][y] > r:
        count+=1
        m[x][y] = 0
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            dfs(m, new_x, new_y, r)

def count_flood(rain_map, r):
    result =[]
    global count
    for mx in range(N):
        for my in range(N):
            if rain_map[mx][my] > r:
                dfs(rain_map, mx, my, r)
                result.append(count)
                count = 0
    ans.append(len(result))


ans =[]
if max_rain == 1:
    print(1)
else:
    for m in range(min_rain, max_rain+1):
        copy_map = copy.deepcopy(map)
        count_flood(copy_map, m)
    print(max(ans))