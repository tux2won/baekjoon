from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(N+1):
    graph[i].sort()



def dfs(graph, v, visited):
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
			
dfs_visited = [False] * (N+1)
dfs(graph, V, dfs_visited)



def bfs(graph, start, visited):
	queue = deque([start])
	visited[start] = True
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
				
bfs_visited = [False] * (N+1)

print()
bfs(graph, V, bfs_visited)