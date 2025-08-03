ip = input() 
stack = [] 
ans = 0
for i in range(len(ip)):
    if ip[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if ip[i-1] == "(":
            ans += len(stack)
        else:
            ans+=1
print(ans)