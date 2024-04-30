n = map(int, input().split())
total_3 = 0
total_5 = 0

for i in n:
    if i % 3 == 0:
        total_3 = total_3 + 1
    if i % 5 == 0:
        total_5 = total_5 +1

print(f"Multiples of 3 : {total_3}")
print(f"Multiples of 5 : {total_5}")