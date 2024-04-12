while True:
    print("1. 입력하기")
    print("2. 출력하기")
    print("3. 삭제하기")
    print("4. 끝내기")

    number = int(input("작업할 번호를 선택하세요."))
    if number == 1:
        print("")
        print("입력하기를 선택하였습니다.")
        print("")
    if number == 2:
        print("")
        print("출력하기를 선택하였습니다.")
        print("")
    if number == 3:
        print("")
        print("삭제하기를 선택하였습니다.")
        print("")
    if number == 4:
        print("")
        print("끝내기를 선택하였습니다.")
        break
    if number > 4 or number < 1:
        print("")
        print("잘못 선택하였습니다.")
        print("")