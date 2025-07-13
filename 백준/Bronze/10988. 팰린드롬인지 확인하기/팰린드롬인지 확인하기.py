w = str(input())
lenth = len(w)

initial_state = 1

for i in range(lenth // 2):
    if w[i] != w[lenth - 1 - i]:
        initial_state = 0
        break
    
print(initial_state)