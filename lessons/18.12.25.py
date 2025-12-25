# numbers = list(map(int, input().split()))
# print(numbers[::2])
# print(numbers.index(min(numbers)))
# numbers.remove(max(numbers))
# print(numbers)
# print(sorted(numbers, reverse = True))


# Дан список:
# list_1 = [1, 2, 3, 4, 2, 3, 4, 6, 8]
# Пользователь вводит одной строкой несколько целых чисел, разделённых пробелом.
# Сформируйте из этих чисел список list_2.
# Напишите программу, которая находит и выводит кортеж,
# состоящий только из общих элементов обоих списков (list_1 и list_2).
# Входные данные:
# 1 3 5 7
# Выходные данные:
# (1, 3)

# list_1 = [
#     1, 2, 3, 4, 2 ,3 ,4, 6 ,8
# ]
# a = map(int, input().split())
# list_2 = []
# for i in a:
#     list_2.append(i)
# print(tuple(set(list_1).intersection(set(list_2))))
# print(tuple(set(list_1) & set(list_2)))

# ASCI - таблица
# print(ord('H'))
# chr
# print(chr(72))


# a = input()
# b = ''
# for i in a:
#     if 64 > ord(i) < 91:
#         b += chr(ord(i) + 32)
#     else:
#         b += i
# print(b)

# s = "HeLLo World"
# result = ''
# for i in s:
#     code = ord(i)
#     if 65 <= code <= 90:
#         result += chr(code + 32)
#     else:
#         result += i
# print(result)





