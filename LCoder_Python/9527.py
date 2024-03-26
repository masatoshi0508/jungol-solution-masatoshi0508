name, kor, eng, mat = input().split()

kor = int(kor)
eng = int(eng)
mat = int(mat)

sum = kor+eng+mat
avg = (kor+eng+mat)/3
avg = "{:.2f}".format(avg)

print("           name  kor  eng  mat  sum    avg")
print("    ", name,"",kor,"  ", eng, " ", mat, "", sum, "", avg) 
print(" ")
print("           name  kor  eng  mat  sum    avg")
print("    ", name,"",kor,"  ", eng, " ", mat, "", sum, "", avg) 