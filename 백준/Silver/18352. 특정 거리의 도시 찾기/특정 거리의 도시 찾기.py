from collections import deque
import sys
f = sys.stdin.readline
N, M, K, X = map(int, f().split())
graph = [[] for _ in range(N+1)]
distance = [0] * (N+1)
visited = [False] * (N+1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
for i in range(N+1):
    graph[i].sort()
def bfs(graph, start, visited):
	queue = deque([start])
	visited[start] = True
	ans = []
	distance[start] = 0
	while queue:
		v = queue.popleft()
		# print(v, end=' ')
		for i in graph[v]:
			if not visited[i]==True:
				queue.append(i)
				visited[i] = True
				distance[i] = distance[v] + 1
				if distance[i] == K:
					ans.append(i)
	if len(ans)==0:
		print(-1)
	else:
		ans.sort()
		for i in ans:
			print(i, end='\n')
bfs(graph, X, visited)