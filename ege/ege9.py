# with open('9.txt', 'r') as f:
#     k = 0
#     for line in f:
#         a = sorted([int(x) for x in line.split()])
#         s = [x for x in a if x % 3 == 0]
#         if len(s) == 3:
#             r = a[5] - a[0]
#             if r <= sum(s):
#                 k += 1
#     print(k)
#
#
#
# # Чтение данных из файла
# # f = open('9.txt')
# # разбить данные по строкам
# # a = f.read().strip().split()
# # разбить строки на отдельные числа
# # for i in range(len(a)):
#     # a[i] = [int(x) for x in a[i].split(';')]
#
# # k = 0  # счетчик подходящих строк
# # перебрать все строки
# # for s in a:
#     r = []  # повторяющиеся числа
#     n = []  # неповторяющиеся числа
#     # разделить числа
#     for c in s:
#         if s.count(c) > 1:
#             r.append(c)
#         else:
#             n.append(c)
#     # только одно число повторяется трижды
#     if len(r) == 3 and len(set(r)) == 1:
#         # утроенный квадрат повторяющегося числа
#         # больше суммы квадратов неповторяющихся чисел
#         if r[0]**2 * 3 > n[0]**2 + n[1]**2 + n[2]**2:
#             # увеличение счетчика
#             k += 1
# print(k)
#
# with open('9.txt', 'r') as f:
#     k = 0
#     for line in f:
#         a = sorted([int(x) for x in line.split()])
#         c = [x for x in a if x % 2 == 0]
#         n = [x for x in a if x % 2 == 1]
#         cond_a = len(set(a)) == 5
#         sr_c = sum(c) / len(c) if c else 0
#         sr_n = sum(n) / len(n) if n else 0
#         cond_b = abs(sr_c - sr_n) > 50
#         if cond_a ^ cond_b:
#             k += 1
#     print(k)


# count = 0

# with open('9.txt') as f:
#     for line in f:
#         nums = list(map(int, line.split()))
#
#         # 1 условие (упрощённое)
#         cond_a = len(nums) - len(set(nums)) == 1
#
#         # 2 условие
#         evens = [x for x in nums if x % 2 == 0]
#         odds = [x for x in nums if x % 2 == 1]
#
#         avg_even = sum(evens) / len(evens) if evens else 0
#         avg_odd = sum(odds) / len(odds) if odds else 0
#
#         cond_b = abs(avg_even - avg_odd) > 50
#
#         # ровно одно условие
#         if cond_a ^ cond_b:
#             count += 1
#
# print(count)



# with open('9.txt') as f:
#     k = 0
#     for line in f:
#         a = sorted([int(x) for x in line.split()])
#         mn = min(a)
#         mx = max(a)
#         if a.count(mn) == 1:
#
#             others = a.copy()
#             others.remove(mn)
#             if len(others) != len(set(others)):
#
#                 summ = 0
#                 for x in set(others):
#                     if others.count(x) > 1:
#                         summ += x * others.count(x)
#                 if mn + mx < summ:
#                     k += 1
#
#     print(k)



# with open('9.txt') as f:
#     k = 0
#     for line in f:
#         a = sorted([int(x) for x in line.split()])
#         rep = [int(x) for x in a if a.count(x) > 1]
#         non_rep = [int(x) for x in a if a.count(x) == 1]
#         if rep and non_rep:
#             avg_ap = sum(rep) / len(rep) if rep else 0
#             avg_np = sum(non_rep) / len(non_rep) if non_rep else 0
#             if avg_np < avg_ap:
#                 k += 1
#     print(k)

# summ = 0
# for line in open('9.txt'):
#     a = sorted([int(x) for x in line.split()])
#     p = [int(x) for x in a if a.count(x) == 2]
#     pp = [int(x) for x in a if a.count(x) == 2]
#     if p and pp and len(set(a)) == 5:
#         if a.count(max(a)) == 1:
#             summ = sum(a)
#             break
# print(summ)



# with open('9.txt') as f:
#     for i, line in enumerate(f,start=1):
#         a = list(map(int, line.split()))
#
#         if len(set(a)) == 5:
#             for x in set(a):
#                 if a.count(x) == 2:
#                     p = x
#
#             s = [x for x in a if a.count(x) == 1]
#             if p >= sum(s) / 4:
#                 break
#
#
#
# print(i)

k = 0
for line in open('../9.txt'):
    a = list(map(int, line.split()))
    if len(set(a)) == 5:
        for x in set(a):
            if a.count(x) == 3:
                t = x
        s = [x for x in a if a.count(x) == 1]
        if sum(s) / 4 <= t:
            k += 1
print(k)






