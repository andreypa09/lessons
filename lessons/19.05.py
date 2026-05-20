# 1.
# a = input()
# print(len(a))

# 2.
# a = input()
# print(a.__contains__('a'))

# 3.
# a = input()
# if a.__contains__('o'):
#     for i in a:
#         if i == 'o':
#             print(a.index(i))
# else:
#     print('В сообщении нет буквы o')

# 4.
# a = input()
# print(a[0].upper() + a[1:])

# 5.
# a = input()
# print(a.upper())
# print(a.lower())

# 6.
# a = input()
# print(a.endswith('ов'))

# 7.
# a = input()
# print(a.rfind('a'))

# 8.
# a = input()
# print(a.isalpha())

# 9.
# a = input()
# for i in a:
#     if i.isdigit():
#         print(i.isdigit())

# 10.
# a = input().split()
# print(','.join(a))

# 11.
# a = input()
# glasnie = 'euioa'
# print(''.join(i for i in a if i not in glasnie))

# 12.
# a = input()
# flag = False
# flag1 = False
# if a.isdigit():
#     print('Только цифры')
# if a.isalpha():
#     print('Только буквы')
# for i in a:
#     if i.isalpha():
#         flag = True
#     if i.isdigit():
#         flag1 = True
# if flag and flag1:
#     print('Буквы и цифры')

# 13.
# a = input()
# for i in a:
#     if i.islower():
#         print("Состоит из прописных")
#         break
#     if i.isupper() and not a.isupper():
#         print("Состоит из заглавных")
#         break
# if a.isupper():
#     print("Написана в виде заголовка")

# 14.
# a = 'a1b2c3d4e5f6g7'
# s = [i for i in a if i.isdigit()]
# print("".join(s))

# 15.
# a = input()
# for i in a:
#     if i.isdigit():
#         a = a.upper()
#         break
# a = a.replace(' ','*')
# print(a)

# 16.
# a = 'abcd defg ghij'
# s = [i for i in a if a.count(i) > 1]
# for i in s:
#     for j in a:
#         if i == j:
#             a = a.replace(j, '')
# print(a)

# 17.
# glasnie = 'euioa'
# k = []
# a = input()
# for i in glasnie:
#     if i in a:
#         k.append(a.rfind(i))
# print(max(k), a[max(k)])

# 18.