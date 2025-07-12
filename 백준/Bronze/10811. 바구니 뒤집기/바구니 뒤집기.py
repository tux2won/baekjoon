n, m = map(int, input().split())
i_list = []
j_list = []
basket = []

cnt = 1
for i in range(n):
    basket.append(cnt)
    cnt+=1

for i in range(m):
    a, b = map(int, input().split())
    i_list.append(a)
    j_list.append(b)

# print(basket)
# print(i_list)
# print(j_list)

for i in range(m):
    start = i_list[i] - 1
    end = j_list[i] - 1
    basket[start:end + 1] = basket[start:end + 1][::-1]
print(' '.join(map(str, basket)))