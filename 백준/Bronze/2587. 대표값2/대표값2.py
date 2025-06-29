num = []

for i in range(5):
    number = int(input())
    num.append(number)

average = int(sum(num) / 5)
med_index=len(num)//2
median = sorted(num)[med_index]
print(average)
print(median)