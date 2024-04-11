while True:
    score = int(input())
    if score % 3 == 0:
        print(f"{score//3}")
    if score == -1:
        break