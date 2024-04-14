odd = 0
even = 0

while True:
    str1 = int(input())
    if str1 == 0:
        break
    if str1 % 2 != 0:
        odd = odd + 1
    if str1 % 2 == 0:
        even = even + 1

print(f"odd : {odd}")
print(f"even : {even}")