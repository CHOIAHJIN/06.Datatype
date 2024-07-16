# # double loop
# # for i in range(1,10) :
# #     for k in range(11, 20) :
#         print(i, k)
# m = [[1,2,3], [4,5,6],[7,8,9]]
# for i in m :
#     for e in i :
#         print(e)

# 연습문제
# num_list = [[10,50], [20, 40], [30, 60], [40, 70]]
# for i in num_list :
#     for e in i :
#         print(e)

# 예제 2 / 내가 푼 방법
# my_list = [[100, 200], [400,800], [1000,1400]]
# for i in my_list :
#     a= (i[0]+i[1])/2
#     print(a)

# # 예제 2 / 교수님이 푼 방법
# my_list = [[100, 200], [400,800], [1000,1400]]
# for i in my_list :
#     var = 0
#     for j in i :
#         var = var + j
#     print(var / len(i))

# 예제 3
# i = 0
# while i < 10 :
#     i = i + 1
#     print("나무를", i, "번 찍었습니다.")
# else :
#     print("나무가 넘어갑니다!")

# 내가 푼 문제
# i = 0
# while i < 10 :
#     i = i + 1
#     print("*"*i)

# # 교수님의 풀이
# for i in range(1,11) :
#     print("*"*i)

# 예제
numbers_1 = []
numbers_2 = []
numbers_3 = []

# for i in range(1,101) :
#     if i % 2 == 0 :
#         numbers_1.append(i)
#     if i % 3 == 0 :
#         numbers_2.append(i)
#     if i % 5 == 0 :
#         numbers_3.append(i)
#
# print(numbers_1)
# print(numbers_2)
# print(numbers_3)

