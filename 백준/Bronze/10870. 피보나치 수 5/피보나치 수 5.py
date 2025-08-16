n = int(input())

num = [0, 1]
for i in range(n-1):
    p = num[i] + num[i+1]
    num.append(p)

print(num[n])