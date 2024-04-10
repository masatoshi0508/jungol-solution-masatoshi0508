count = 0
total = 0

while True:
    score = int(input())
    if score == 0:
        break
    if score % 2 != 0:
        count = count + 1
        total = total + score

avg = total // count

print(f"""
홀수의 합 = {total}
홀수의 평균 = {avg}
""")