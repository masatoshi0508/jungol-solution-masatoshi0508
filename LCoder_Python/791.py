a, b = input().split()
c, d = input().split()

list1 = [int(a)] * int(b)
list2 = [int(c)] * int(d)

list3 = list1 + list2

print(list3)