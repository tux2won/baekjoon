div_num = int(input())
div_list = list(map(int, input().split()))
max_div = max(div_list)
min_div = min(div_list)

print(max_div * min_div)