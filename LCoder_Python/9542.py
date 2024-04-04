menu1 = "삽입"
menu2 = "수정"
menu3 = "삭제"

print("""1. 삽입
2. 수정
3. 삭제""")

menu = int(input("메뉴를 선택하세요. "))

if menu == 1:
    print("{}을 선택하셨습니다.".format(menu1))
elif menu == 2:
    print("{}을 선택하셨습니다.".format(menu2))
else:
    print("{}을 선택하셨습니다.".format(menu3))