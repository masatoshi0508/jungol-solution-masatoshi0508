n = map(int, input().split())
count = 0

for i in n:
    if i % 2 == 0:
        count = count + 1

print(f"입력받은 짝수는 {count}개입니다.")