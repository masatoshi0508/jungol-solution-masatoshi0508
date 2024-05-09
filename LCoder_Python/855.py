x, y = map(int, input().split())
sum = 0
count = 0

if x < y:
    for i in range(x, y+1):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
            count = count + 1
elif x > y:
    for i in range(y, x+1):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
            count = count + 1
else:
    sum = sum + x
    count = count + 1

avg = sum / count

print(f"sum : {sum}")
print(f"avg : {avg:.1f}")