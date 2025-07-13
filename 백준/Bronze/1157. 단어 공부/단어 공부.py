w = input()
lenth = len(w)
w=w.lower()
cnt = [0] * 26

for i in range(lenth):
    idx = ord(w[i]) - ord('a')
    cnt[idx] += 1

max_count = max(cnt)    
max_count_num = cnt.count(max_count)

if max_count_num > 1:
    print("?")
else:
    max_index = cnt.index(max_count)
    print(chr(max_index + ord('A')))