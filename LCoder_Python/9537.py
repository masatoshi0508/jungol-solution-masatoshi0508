a, b = input().split()

a = int(a)
b = int(b)

if a > b:
    print("입력받은 수 중 큰 수는 {} 이고 작은 수는 {} 입니다.".format(a, b))
else:
    print("입력받은 수 중 큰 수는 {} 이고 작은 수는 {} 입니다.".format(b, a))