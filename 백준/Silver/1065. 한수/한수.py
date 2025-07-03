N = int(input())
count=0
num_list=list(map(int, str(N)))
for i in range(1, N+1):
    num_list=list(map(int, str(i)))
    if len(num_list) <=2:
        count += 1
    else:
        ans = num_list[0] - num_list[1]
        for j in range(1, len(num_list)-1):
            if num_list[j]-num_list[j+1] != ans:
                break
            else:
                count += 1
print(count)