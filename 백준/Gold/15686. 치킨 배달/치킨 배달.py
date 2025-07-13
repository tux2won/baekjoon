from itertools import combinations
N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        if city[i][j] == 2:
            chicken.append((i,j))
chicken_candidates = list(combinations(chicken, M))
total_dist_list = []
for cc in chicken_candidates:
    total_dist = 0
    for hx, hy in home:
        min_dist_list = []
        for cx, cy in cc:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist_list.append(dist)
        min_dist = min(min_dist_list)
        total_dist += min_dist
        min_dist_list.clear()
    total_dist_list.append(total_dist)
ans = min(total_dist_list)
print(ans)