str1, str2 = input().split()
str1 = int(str1)
str2 = int(str2)

if str1 > str2:
    print(str1 - str2)
else:
    print(str2 - str1)