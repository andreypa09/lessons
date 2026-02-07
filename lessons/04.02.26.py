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

# import sys
# from functools import lru_cache
# sys.setrecursionlimit(10000)
# @lru_cache(maxsize=2 ** 8)
# def tribonachi(n):
#     if n < 2:
#         return n
#     if n == 2:
#         return 1
#     return tribonachi(n - 1) + tribonachi(n - 2) + tribonachi(n - 3)
# print(tribonachi(10))



# from functools import lru_cache
# @lru_cache()
# def trap(n):
#     if n < 1:
#         return 1
#     if n == 1:
#         return 1
#     return trap(n-1) + trap(n-2)
# print(trap(9))



# 1. Решите задачу о Ханойских башнях для n дисков. Выведите последовательность ходов.
# Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3.
# На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра.
# Диски можно перекладывать с одного стержня на другой по одному, при этом диск нельзя класть на диск меньшего диаметра.
# Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
import sys
sys.setrecursionlimit(10000)
# from functools import lru_cache
#
# @lru_cache(maxsize=None)

# def hanoi(n, source, target, auxiliary, moves = []):
#     if n == 1:
#         moves.append(f"Pереместить диск 1 с {source} на {target}")
#         return moves
#     hanoi(n - 1, source, auxiliary, target, moves)
#
#     moves.append(f'переместить диск {n} с {source} на {target}')
#
#     hanoi(n-1, auxiliary, target, source, moves)
#     return moves
# movesl = hanoi(3, "A", "C", "B")
# for move in movesl:
#     print(move)
# print(f"Всего ходов {len(movesl)}")



