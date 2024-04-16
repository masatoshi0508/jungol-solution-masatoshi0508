count = 0

while True:
    str1 = int(input())
    if str1 == 0:
        break
    count = count + 1
    if str1 % 3 == 0 or str1 % 5 == 0:
        count = count - 1

print(count)