from time import *
# def parent(func):
#     def retry(max_retries, delay):
#         for i in range(max_retries):
#             a = func()
#             print(f'Попытка подключения {i}')
#             if a:
#                 print('Успешно')
#                 return a
#             print('Переподключение')
#             sleep(delay)
#         return False
#     return retry
# @parent
# def test():
#     return False
# print(test(3,3))

# def recursion(num):
#     return recursion(num ** 2)
# recursion(1)

# school = [
#     [
#         ['a', 'b', 'c'],['a','b','c'],['a','b','c'],['a','b'],['a']
#     ],
#     [
#         ['a', 'b', 'c'],['a','b','c'],['a','b','c'],['a','b'],['a']
#     ]
# ]
# summ = 0
# for school_item in school:
#     for class_item in school_item:
#         for sym in class_item:
#             summ += 1
# print(summ)
# summ = 0
# def school_ref(school):
#     global summ
#     if len(school) == 1:
#         summ += 1
#         return
#     for i in school:
#         return school_ref(i)
# print(school_ref(school), summ)
#
# a = [
#     1,2,3,
#     4,5,6,
#     7,8,9
# ]
# def rec():
#     summ = 0
#     for i in a:
#         summ += i
#     return summ
# print(rec())

# def rec(lst):
#     if not lst:
#         return 0
#     return lst[0] + rec(lst[1:])
# print(rec(a))

# def reverse_str(s):
#     result = ''
#     for char in s:
#         result += char + result
#     return result
# def reverse_rec(s):
#     if len(s) <= 1:
#         return s
#     return reverse_rec(s[1:]) + s[0]
# print(reverse_rec('hello'))


# факториал рекурсивно
# start = time()
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# fact(10)
# end = time()
# print(end-start)

#
# import sys
# # print(sys.getrecursionlimit())
# sys.setrecursionlimit(15000000)
# start = time()
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# fact(1000000)
# end = time()
# print(end-start)

# def A():
#     return B()
# def B():
#     return C()
# def C():
#     pass
# A()

# POP -
# PUSH - добавление элемента в стек