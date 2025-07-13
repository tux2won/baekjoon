N = int(input())
score = str(N)
mid = len(score)//2
front =score[0:mid]
back = score[mid:len(score)]
front_sum = 0
back_sum = 0
for i in range(len(front)):
    front_sum += int(front[i])
    back_sum += int(back[i])
if front_sum == back_sum:
    print("LUCKY")
else:
    print("READY")