while True:
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    number = int(input("number? "))
    if number == 1:
        print("Seoul")
    if number == 2:
        print("Washington")
    if number == 3:
        print("Tokyo")
    if number == 4:
        print("Beijing")
    if number < 1 or number > 4:
        print("none")
        break