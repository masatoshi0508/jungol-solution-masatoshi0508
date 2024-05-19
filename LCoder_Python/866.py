n = int(input())

for i in range(n, 0, -1):
    star = "*" * (2*i-1) 
    print(star.center(2*n-1))