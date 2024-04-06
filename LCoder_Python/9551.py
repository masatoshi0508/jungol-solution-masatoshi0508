num = 1
total =0

while num <= 10:
    total = total + num
    num = num + 1

print("1부터 10까지의 합 = {}".format(total))
print("while문이 끝난 후의 num의 값 = {}".format(num))


# # 변수 num에 1을 대입
# num = 1
# # 누적 합을 저장할 변수 초기화
# total = 0

# # while문을 이용하여 1부터 10까지의 누적 합 구하기
# while num <= 10:
#     total += num  # total에 num을 더함
#     num += 1      # num을 1씩 증가시킴

# # 1부터 10까지의 합 출력
# print("1부터 10까지의 합 =", total)
# # while문이 끝난 후의 num 값 출력
# print("while문이 끝난 후의 num의 값 =", num)