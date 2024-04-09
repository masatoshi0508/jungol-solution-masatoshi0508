count = 0
total = 0

while True:
    score = int(input())
    if score >= 100:
        break
    count = count + 1
    total = total + score

count = count + 1
total = total + score
avg = total / count

print(total)
print(f"{avg:.1f}")