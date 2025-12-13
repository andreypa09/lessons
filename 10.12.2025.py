# Откройте файл 900,
# содержащий в каждой строке шесть натуральных чисел.
# Определите количество строк, содержащих числа,
# для которых выполнены оба условия:
# в строке только одно число повторяется трижды,
# остальные числа различны;
# квадрат суммы всех повторяющихся чисел строки больше квадрата суммы
# всех её неповторяющихся чисел.

# with open("900.txt", "r") as f:
#     amount_lines = 0
#     for line in f:
#         numbers = line.split("\t")
#         s = []
#         for i in numbers:
#             s.append(int(i))
#         counter = 0
#         first = []
#         second = []
#         for i in s:
#             if s.count(i) != 1:
#                 first.append(i)
#                 continue
#             second.append(i)
#         if len(s) == 4 and sum():
#             amount_lines += 1
#
#     print(amount_lines)




# with open("905.txt", "r") as f:
#     counter = 0
#     for line in f:
#         numbers = line.split("\t")
#         s = []
#         for i in numbers:
#             s.append(int(i))
#         if len(set(s)) == 3 and s.count(max(s)) > 1:
#             counter += 1
#     print(counter)
#
#
# hw
# 1. with open("907.txt", "r") as f:
#     counter = 0
#     for line in f:
#         numbers = line.split("\t")
#         s = []
#         for i in numbers:
#             s.append(int(i))
#             s = sorted(s)
#
#
#
#
#     print(counter)
# 2.
# with open("908.txt", "r") as f:
#     s = []
#     for line in f:
#         a = map(int, line.split())
#         s.append(sum(a))
#     print(min(s) - sum(s)/len(s))



