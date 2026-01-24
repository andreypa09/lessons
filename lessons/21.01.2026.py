# map(функция, список(итерируемый объект))
# map - Это метод, который позволяет применить функцию к каждому элементу последовательности


# def plus5(x):
#     return x + 5
# a = [1,1,1,1,1]
# print(list(map(lambda x: x + 5, a)))

# user = [
#     {"username": "daniel", "age": 10},
#     {"username": "daniel1", "age": 10},
#     {"username": "daniel2", "age": 10},
#     {"username": "daniel3", "age": 10}
# ]
# print(list(map(lambda x: x["username"], user)))

# filter()
# nums = list(range(10))
# [0,1,2,3,4,5,6,7,8,9]
# [True,False ... False]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# def plus():

# def minus():

# def ss(fplus, fminus):
#     return fplus, fminus




# nums = [1, 2 , 3, 4, 5]
# square_nums = list(map(lambda x: x * x, nums))
# print(square_nums)
#
# nums = list(range(1,11))
# not_evens = list(filter(lambda x: x % 2 == 1, nums))
# print(not_evens)

# words = ['apple', 'banana', 'cherry', 'date']
# len_words = list(map(len, words))
# print(len_words)

# nums = [-5, -2, 0, 3, 7, -1, 10]
# positive_nums = list(filter(lambda num: num >= 0, nums))
# print(positive_nums)

# a = [1,1,1,1,1,1]
# b = [2,2,2,2,2,2]
# print(list(map(lambda x,y: x + y, a, b)))

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# print(list(map(lambda x,y: x * y, list1, list2)))

# def is_simple(x):
#     if 0 <= x <= 2:
#         return False
#     for i in range(2, int(x / 2) + 1):
#         if x % i == 0:
#             return False
#     return True
# nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list(filter(is_simple, nums)))

# def my_map(lambda1, nums1):
#     result = []
#     for num in nums1:
#         result.append(lambda1(num))
#     return result
# nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(my_map(lambda x: x, nums))



# hw.
# def my_filter(lambda1,nums):
#     result = []
#     result1 = []
#     for i in nums:
#         result.append(lambda1(i))
#         result1 = [num for num in result if lambda1(i) == 1]
#     return result1
# print(my_filter(lambda x:x%2 == 0,[1,2,3,4,5]))
# не смог

# 2.
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
# new_list1 = list(map(lambda x,y: x + y, list1, list2))
#
# print(list(filter(lambda x: x >= 40, new_list1)))


# 3.
nums = list(range(-10, 11))
print(list(filter(lambda x: x > 3 or x < -3, nums)))
nums = list(map(lambda x: x ** 2, nums))
nums = list(filter(lambda x: x % 10 < 5, nums))
print(nums[:5])

