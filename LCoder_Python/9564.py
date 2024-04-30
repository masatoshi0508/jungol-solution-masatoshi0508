score = map(int, input().split())
total = 0
count = 0

for i in score:
    total = total + i
    count = count + 1

avg = total / count

print(f"총점 : {total}")
print(f"평균 : {avg}")