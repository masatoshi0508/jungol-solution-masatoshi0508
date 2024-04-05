str1, str2, str3 = input().split()
str1 = int(str1)
str2 = int(str2)
str3 = int(str3)

if str1 < str2 and str1 < str3:
    print(str1)
elif str2 < str1 and str2 < str3:
    print(str2)
elif str3 < str1 and str3 < str2:
    print(str3)
elif str1 == str2 or str1 == str3:
    print(str1)
else:
    print(str2)