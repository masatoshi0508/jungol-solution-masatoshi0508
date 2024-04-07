while True:
    score = int(input("점수를 입력하세요. "))
    if score > 100 or score < 0:
        break
    if score >= 80:
        print("축하합니다. 합격입니다.")
    if score < 80:
        print("죄송합니다. 불합격입니다.")