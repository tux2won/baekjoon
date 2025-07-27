A, B = map(int, input().split())
C = int(input())

hour = C // 60
min = C % 60
A = A + hour
B = B + min

if B >= 60:
    A += B//60
    B = B % 60

if A >= 24:
    A = A % 24

print(A, B)