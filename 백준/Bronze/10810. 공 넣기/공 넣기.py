N, M = map(int, input().split())
basket = ['0']*N

for _ in range(M):
    i, j, k = map(int, input().split())
    for put_num in range(i-1, j):
        basket[put_num] = str(k)

print(' '.join(basket))