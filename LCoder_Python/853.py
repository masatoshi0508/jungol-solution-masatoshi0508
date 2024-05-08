n = map(int, input().split())
total = 0
count = 0

for i in n:
    total = total + i
    count = count + 1

avg = total / count

print(f"{avg:.2f}")