while True:
    score = int(input("(입력)"))
    if score % 3 == 0:
        print(f"(출력){score//3}")
    if score == -1:
        break