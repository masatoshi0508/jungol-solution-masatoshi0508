list = ['Carrot', 'Onion', 'Cabbage', 'Potato', 'Sweet Potato', 'Bean']

original_list = list.copy()

print("첫 번째 원소:", list[0])
print("마지막 원소:", list[5])

list.reverse()

print("리스트 거꾸로 출력하기:", list)

list = original_list

print("li[2:5]:", list[2:5])
print("li[5:2:-1]:", list[5:2:-1])
print("li[1:6:2]:", list[1:6:2])