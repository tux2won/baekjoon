a = []
n = int(input())
for i in range(n):
    t = int(input())
    a.append(t)

a.sort()
for i in range(n):
    print(a[i]) #순서대로 꺼내와