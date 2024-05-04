num1 = 2
num2 = 4

for i in range(1, 10):
    for j in range(num1, num2+1):
        print(f"{j} * {i} = {j*i:2}", end="  ")
    print()