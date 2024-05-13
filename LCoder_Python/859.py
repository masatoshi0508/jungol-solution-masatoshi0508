row, column = map(int, input().split())

if row > column:
    for i in range(1, 10):
        for j in range(row, column-1, -1):
            print(f"{j} * {i} = {i*j:2}", end="   ")
        print()
elif row < column:
    for i in range(1, 10):
        for j in range(row, column+1):
            print(f"{j} * {i} = {i*j:2}", end="   ")
        print()
else:
    for i in range(1, 10):
        for j in range(row, row+1):
            print(f"{j} * {i} = {i*j:2}", end="   ")
        print()