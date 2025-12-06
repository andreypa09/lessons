# ascii_letters, ascii_uppercase, ascii_lowercase

# digits, punctuation

# s = "sadsaddsasafasfaf"
# import string
#
# print(string.punctuation)
# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_uppercase)

# print("hello" + ":" + "world")
# aaa = ":"
# print(f"hello{aaa}world")


# 1.
# from random import randint, choice
# import string
# list_pairs = []
# for i in range(100):
#     a = choice(string.ascii_uppercase)
#     a += str(randint(0, 9)) + "\n"
#     list_pairs.append(a)
# with open("cw.txt", "w+") as file:
#     file.writelines(list_pairs)
# with open("cw.txt", "r") as file:
#     for i in file:
#         if int(i[1]) % 2 == 0 and i[1] != "0":
#             print(i)
#             break
#
#
#
#
# with open ("cw.txt", "r") as file:
#     # cnt = 0
#     # for i in file:
#     #     if i[0] == "A":
#     #         cnt += 1
#     # print(cnt)
#     a = "".join(file.readlines()).count("A")
#     print(a)


# from random import randint, choice
# import string
# list_pairs = []
# for i in range(150):
#     a = choice(string.ascii_uppercase)
#     a += f"-{randint(0,9)}\n"
#     list_pairs.append(a)
# with open("cw.txt", "w") as file:
#     file.writelines(list_pairs)
# with open("cw.txt", "r") as file:
#     for i in file:
#         print(i)
#         if int(i[2]) > 5:
#             print(i)


import string
with open("903.txt", "r") as f:
    for line in f:
        numbers = line.split("\t")
        maxim = 0
        minim = 999999999999
        for i in numbers:
            if int(i) > maxim:
                maxim = int(i)
            if int(i) < minim:
                minim = int(i)
        print(numbers, maxim, minim)




