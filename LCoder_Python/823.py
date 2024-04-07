while True:
    number = int(input("number? "))
    if number == 0:
        break
    if number > 0:
        print("positive integer")
    if number < 0:
        print("negative number")