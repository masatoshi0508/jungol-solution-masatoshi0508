score = map(int, input().split())
count = 0
total = 0

for i in score:
    count = count + 1
    total = total + i

avg = total / count
print(f"avg : {avg:.1f}")

if avg >= 80:
    print("pass")
else:
    print("fail")