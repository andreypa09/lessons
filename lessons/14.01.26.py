# 3 dz. matrix = [[i * 4 + j + 1 for j in range(4)] for i in range(4)]
#
# print(matrix)

# matrix = [[i * 4 + j + 1 for j in range(4)] for i in range(4)]
# for row in matrix:
#     print(row)

# Создайте словарь, где ключами являются числа от 1 до 10, а значениями - их кубы

# cubes_dict = {x:x ** 3 for x in range(1,11)}
# print(cubes_dict)

# Создайте множество квадратов чисел от 1 до 20.
# mz = {a ** 2 for a in range(1, 21)}
# print(mz)

# Дан список чисел [2, 4, 6, 8, 10]. Проверьте, есть ли в списке хотя бы одно число, которое больше 7 И делится на 3.
# list_1 = [2, 4, 6, 8, 10]
# result = any(i > 7 and i % 3 == 0 for i in list_1)
# print(result)

# Дан пароль password = "MyPass123". Проверьте, что пароль содержит хотя бы одну заглавную букву,
# одну строчную букву и одну цифру.
# password = "MyPass123"
# has_upper = any(i.isupper() for i in password)
# has_lower = any(i.islower() for i in password)
# has_digit = any(i.isdigit() for i in password)
# all_us = (has_upper, has_lower, has_digit)
# print(all(all_us))

# Дан словарь с ценами prices = {'яблоки': 100, 'бананы': 80, 'апельсины': 120, 'груши': 90}.
# Проверьте, все ли цены находятся в диапазоне от 50 до 150 рублей.
# prices = {'яблоки': 100, 'бананы': 80, 'апельсины': 120, 'груши': 90}


# Определите наибольший номер строки таблицы, для чисел которой выполнены оба условия:
#     в строке есть ровно два числа, каждое из которых повторяется трижды, и одно число без повторений;
#     среднее арифметическое повторяющихся чисел строки меньше неповторяющегося числа.

# with open('901.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
# def f1(line):
#     cnt_3 = [i for i in line if line.count(i) == 3]
#     cnt_1 = [i for i in line if line.count(i) == 1]
#     return len(cnt_3) == 6 and len(cnt_1) == 1
# def f2(line):
#     # Повторяющиеся
#     rep = [i for i in line if line.count(i) != 1]
#     # Неповторяющиеся
#     not_rep = [i for i in line if line.count(i) == 1]
#     # Ср ариф.
#     aver = sum(rep) / len(rep)
#     return aver < not_rep[0]
#
# for pos, val in list(enumerate(data, start = 1))[::-1]:
#     if f1(val) and f2(val):
#         print(pos)
#         break


# Определите наибольший номер строки таблицы, для чисел которой выполнены оба условия:
#     в строке есть одно число, которое повторяется трижды, остальные три числа различны;
#     повторяющееся число строки больше, чем среднее арифметическое её неповторяющихся чисел.

# 1 СПОСОБ
# with open('911.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
# def f1(line):
#     cnt_3 = [i for i in line if line.count(i) == 3]
#     others_nums = [i for i in line if line.count(i) == 1]
#     return len(cnt_3) == 3 and len(others_nums) == 3
# def f2(line):
#     rep = [i for i in line if line.count(i) != 1]
#     norep = [i for i in line if line.count(i) == 1]
#     aver_norep = sum(norep) / len(rep)
#     return rep[0] > aver_norep
# for pos, val in list(enumerate(data, start = 1))[::-1]:
#     if f1(val) and f2(val):
#         print(pos)
#         break
# 2 Способ
# from statistics import mean
# mean - ср.ариф
# with open('911.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
# for pos, val in list(enumerate(data, start = 1))[::-1]:
#     cnt_3 = [i for i in val if val.count(i) == 3]
#     cnt_1 = [i for i in val if val.count(i) == 1]
#     if len(cnt_3) == 3 and len(cnt_1) == 3 and mean(cnt_1) < cnt_3[0]:
#         print(pos)
#         break


# Определите наибольший номер строки таблицы, для которой выполнены оба условия:
#     в строке все числа различны;
#     удвоенная сумма минимального и максимального чисел строки равна утроенной сумме трёх её оставшихся чисел.
# with open('913.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
# for pos, val in list(enumerate(data, start = 1))[::-1]:
#     norep = [i for i in val if val.count(i) == 1]
#     maxi = max(val)
#     mini = min(val)
#
#
#     if (maxi + mini) * 2 == sum() * 3:
#         print(pos)
#         break


# hw 1.Определите сумму чисел в строке с наибольшим номером, для которой выполнены оба условия:
# — в строке есть одно число, которое повторяется трижды, остальные четыре числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше повторяющегося числа.
# from statistics import mean
# with open('914.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
# def f1(line):
#     cnt_3 = [i for i in line if line.count(i) == 3]
#     not_rep = [i for i in line if line.count(i) == 1]
#     return len(cnt_3) == 3 and len(not_rep) == 4
# def f2(line):
#     not_rep = [i for i in line if line.count(i) == 1]
#     rep = [i for i in line if line.count(i) != 1]
#     return mean(not_rep) <= rep[0]
# for pos, val in list(enumerate(data, start = 1))[::-1]:
#     if f1(val) and f2(val):
#         print(sum(val))
#         break

# hw 2.Определите количество строк таблицы, для чисел которых выполнены оба условия:
# – в строке все числа различны;
# – сумма двух наибольших чисел строки не больше суммы трёх её оставшихся чисел.
with open("907.txt") as f:
    data = [list(map(int, i.split())) for i in f]
def f1(line):
    return len(set(line)) == 5
def f2(line):
    sorted_line = sorted(line)
    return sorted_line[4] + sorted_line[3] <= sum(sorted_line[:3])
count = 0
for line in data:
    if f1(line) and f2(line):
        count += 1

print(count)
