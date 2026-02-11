# codes = {
#     '200': [],
#     '401': [],
#     '403': [],
#     '404': [],
#     '500': []
# }
#
# with open('access.txt') as f:
#     for line in f:
#         new_line = line.strip()
#         ip = line[:12]
#         kod = new_line[-3:]
#
#         if kod in codes:
#             codes[kod].append(ip)
#
# for code, ipl in codes.items():
#     print(f"Код {code}: {ipl}")



# Задание 3
# Есть файл "triples.txt", который содержит 500 строк, в каждой строке — натуральное число от 1 до 1000.
# Нужно посчитать количество троек последовательных чисел (a, b, c), которые удовлетворяют условию:
# Хотя бы один элемент тройки при делении на 5 даёт остаток, равный минимальному элементу тройки.
# Под тройкой подразумевается три идущих подряд числа в файле.

# with open('triples.txt') as f:
#     data = [list(map(int, i.split()))for i in f]
# for i, num in enumerate(data):
#     for j in range(0, len(data), 3):
#         troyka = [



# f = open("transaction.txt", "r")
# data = f.readlines()
# e = 0
# print("╔══════════════════════════════════════════════════════════╗")
# print("║                    ФИНАНСОВЫЙ ОТЧЕТ                      ║")
# print("╠══════════════════════════════════════════════════════════╣")
# for line in data:
#     line = line.strip()
#     if line == "":
#         continue
#     t = line.split(",")
#     y = t[0].strip()
#     u = t[1].strip()
#     i = float(t[2].strip())
#     e = e + i
#     h = "{:.2f}".format(i) + " ₽"
#     print("║", y, "║", u, "║", h, "║")
# print("╠══════════════════════════════════════════════════════════╣")
# print("║ ИТОГО:", "{:.2f}".format(e), "₽ ║")
# print("╚══════════════════════════════════════════════════════════╝")


