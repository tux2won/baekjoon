num = []
for i in range(10):
    number = int(input())
    num.append(number)

ans = []
for i in num:
    k = i%42
    ans.append(k)
    
cnt = 0
unique = []

for k in ans:
    if k not in unique:
        unique.append(k)
        cnt += 1

print(cnt)