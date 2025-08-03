N = int(input())
cnt = 0
gomgom = []

for _ in range(N):
    chat = input()
    if chat == "ENTER":
        cnt += len(set(gomgom))
        gomgom = []  #초기화
    else:
        gomgom.append(chat)

cnt += len(set(gomgom))
print(cnt)