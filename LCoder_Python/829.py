count = 0
sum = 0

while True:
    score = int(input())
    if score > 100 or score < 0:
        break
    count = count + 1
    sum = sum + score

avg = sum / count

print(f"sum : {sum}")
print(f"avg : {avg:.1f}")