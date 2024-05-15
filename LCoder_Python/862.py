str_1, str_2 = input().split()
str_1 = ord(str_1)
str_2 = ord(str_2)

if str_1 < str_2:
    for i in range(str_1, str_2+1):
        print(chr(i), end=" ")
elif str_1 > str_2:
    for i in range(str_1, str_2-1, -1):
        print(chr(i), end=" ")
else:
    print(chr(str_1))