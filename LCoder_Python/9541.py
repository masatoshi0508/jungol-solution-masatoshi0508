num1, num2, num3 = input("세 수를 입력하세요. ").split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 or num1 > num3:
    print("입력받은 수중 가장 큰 수는 {}입니다.".format(num1))
elif num2 > num3 or num2 > num1:
    print("입력받은 수중 가장 큰 수는 {}입니다.".format(num2))
else:
    print("입력받은 수중 가장 큰 수는 {}입니다.".format(num3))