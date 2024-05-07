x, y = input().split()
x = int(x)
y = int(y)

if x > y:
    for i in range(y, x+1):
        print(i, end=" ")
elif x < y:
    for i in range(x, y+1):
        print(i, end=" ")
else:
    print(x)