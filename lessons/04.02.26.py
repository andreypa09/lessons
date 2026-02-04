# 1.
# Напишите рекурсивную функцию для вычисления a^n (a в степени n).
# def stepen(a, n):
#     if n == 0:
#         return 1
#     return a * stepen(a, n-1)
# print(stepen(5, 2))

# 2.
# Напишите рекурсивную функцию для нахождения суммы цифр числа.
# def sum_digits(num):
#     summ = 0
#     if num == 0:
#         return 0
#     summ += num % 10
#     return summ + sum_digits(num // 10)
# result = sum_digits(101)
# print(result)


# from time import time
# time() - time()
# start = time()
# s = {}
# def fibonacci(n):
#     if n in s:
#         return s[n] -> мемоизация
#     if n < 2:
#         return n
#     result = fibonacci(n-1)+fibonacci(n-2)
#     s[n] = result -> кеширование
#     return result
# #
# print(fibonacci(100))
# print(time()- start)


# !!!
# import time
# from functools import lru_cache
# @lru_cache(maxsize=2 ** 8)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
# start = time.perf_counter()
# print(fib(100))
# end = time.perf_counter()
# print(end - start)
# info = fib.cache_info()
# print(info)
# print(101 * 8)
# !!!

# стек - LIFO - last in first out - пирамида
# очередь - FIFO - first in first out - 0 1 2 3 4
# LFU - least frequency used - Библиотека - чаще всего сохраняются, реже всего удаляются (на сколько часто)
# LRU - least recently used - наименее недавно использованный (время)
# import sys
# sys.setrecursionlimit(10000)
# def f(n):
#     if n < 5:
#         return n
#     return 2 * n*f(n-4)
# print((f(13766) - 9 * f(13762))/ f(13758))


# import sys
# sys.setrecursionlimit(10000)
# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return 2 * n * f(n - 1)
#     return n
# print((f(2024)/16-f(2023))/f(2022))

import sys
from functools import lru_cache
sys.setrecursionlimit(10000)
@lru_cache(maxsize=2 ** 8)
def tribonachi(n):
    if n < 3:
        return n
    return tribonachi(n - 1) + tribonachi(n - 2) + tribonachi(n - 3)
print(tribonachi(10))