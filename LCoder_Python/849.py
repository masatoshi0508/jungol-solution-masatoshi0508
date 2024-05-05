num1 = 2
num2 = 4

for i in range(num1, num2+1):
    for j in range(1, 6):
        print(f"{i} * {j} = {i*j:2}", end="   ")
    print()