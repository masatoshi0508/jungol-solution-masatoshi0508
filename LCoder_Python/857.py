x, y = map(int, input().split())
#xが縦、yが横
matrix = []

for i in range(1, x+1):
    x = []
    for j in range(1, y+1):
        element = i * j
        x.append(element)
    matrix.append(x)

for x in matrix:
    for element in x:
        print(element, end=" ")
    print()