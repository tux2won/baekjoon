N = int(input())
A = list(map(int, input().split())) 
B = list(map(int, input().split()))
A.sort()
B.sort()
S = 0
for i in range(N):
    S += A[i]*B[-(i+1)]
print(S)