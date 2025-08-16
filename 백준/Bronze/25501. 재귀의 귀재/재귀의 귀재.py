T = int(input())

S = []
for _ in range(T):
    i = str(input())
    S.append(i)

def recursion(s, l, r):
    global cnt
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        cnt+=1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global cnt
    cnt +=1
    return recursion(s, 0, len(s)-1)

for i in S:
    cnt = 0
    res, cnt_res = isPalindrome(i)
    print(res, cnt_res)