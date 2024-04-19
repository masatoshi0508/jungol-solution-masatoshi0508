n = int(input())
list1 = []

for i in range (1, n+1):
    list1.append(i)
    list1.reverse()
    list1.sort(reverse=True)

print(list1)