# startwith()
# s = 'Hello World'
# b = 'Hello'
#
# print(s.startswith(b))


# def startwith(st1, st2):
#     if st1 < st2:
#         return False
#     else:
#         for i in range(len(st2)):
#             if st2[i] != st1[i]:
#                 return False
#     return True
# print(startwith('hello world', 'hello '))
# print(startwith('hello', 'world'))




# def count(st, substring):
#     k = 0
#     if st < substring:
#         return False
#     else:
#         for i in range(len(st)):
#             flag = False
#             for j in range(len(substring)):
#                 if st[i + j] != substring[j]:
#                     flag = True
#                     break
#             if not flag:
#                 k += 1
#     return k
# print(count('hello world hello world', 'hello'))
#
# print(count('Hello World Hello WOrld Hello', 'Hello'))

# def count(sr, substr):
#     k = 0
#     a = sr.split(substr)
#     for i in a:
#         if i == ' ':
#             k += 1
#     return k
# print(count('war hellohello war hello python', 'hello'))


def replace(st, old, new):
    string = ''
    if old not in st:
        return False
    else:
        for i in range(len(st)):
            flag = False
            for j in range(len(old)):
                if st[i + j] != old[j]:
                    flag = True
                    break
            if not flag:
                string += new
                i += len(old)
            else:
                string += st[i]
                i += 1
    return string
print(replace('hello world hello python', 'hello', 'hi'))


