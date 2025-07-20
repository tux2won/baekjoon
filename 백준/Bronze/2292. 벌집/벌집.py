n = int(input())

# 벌집의 개수, 1은 무조건 포함
nums = 1 
cnt = 1
while n > nums :
    nums += 6*cnt  # 6의 배수
    cnt += 1
print(cnt)