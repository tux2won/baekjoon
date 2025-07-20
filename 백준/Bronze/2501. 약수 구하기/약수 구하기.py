N, K = map(int, input().split())

div_num = []
i=1
while i <= N:
    if N%i==0:
        div_num.append(i)
        i+=1
    else:
        i+=1
div_num.sort()
if len(div_num) >= K:
    print(div_num[K-1])
else:
    print(0)