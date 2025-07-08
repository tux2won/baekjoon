N = int(input())
map = [list(map(int, input())) for _ in range(N)]
result = []
count = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y):
	global count
	if x<0 or x>=N or y<0 or y>=N:
		return
	if map[x][y] == 1:
		count +=1
		map[x][y] = 0
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			dfs(nx, ny)
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0
result.sort()
print(len(result))
for k in result:
    print(k)