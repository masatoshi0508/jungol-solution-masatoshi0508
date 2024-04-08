count = 0
total = 0

while True:
    number = int(input())
    if number == 0:
        break
    count = count + 1
    total = total + number

print("입력된 자료의 개수 = {}".format(count))
print("입력된 자료의 합계 = {}".format(total))

avg = total / count

print("입력된 자료의 평균 = {:.2f}".format(avg))