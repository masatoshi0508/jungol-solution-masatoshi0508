weight = float(input())

if weight > 88.45:
    print("Heavyweight")
elif 88.45 >= weight > 72.57:
    print("Cruiserweight")
elif 72.57 >= weight > 61.23:
    print("Middleweight")
elif 61.23 >= weight > 50.80:
    print("Lightweight")
else:
    print("Flyweight")