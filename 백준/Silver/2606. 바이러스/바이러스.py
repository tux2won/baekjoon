C = int(input())
C_pair = int(input())

graph = [[] for _ in range(C+1)]

for _ in range(C_pair):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(C+1):
    graph[i].sort()


def dfs(graph, v, visited):
	visited[v] = True
	# print(v, end=' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
			
dfs_visited = [False] * (C+1)
dfs(graph, 1, dfs_visited)

count = 0
for i in dfs_visited:
	if i == True:
		count +=1
print(count-1)