name, height, weight = input().split()

height = int(height)
weight = float(weight)

print("{}의 키는 {}cm이며, 몸무게는 {:.1f}kg입니다.".format(name, height,weight))