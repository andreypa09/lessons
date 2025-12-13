
# with open("task_6.txt","r") as f:
#      a=f.read()
#      max_len=0
#      cur_len=0
#      for i in range(1,len(a)):
#          if (a[i].isdigit() and a[i-1].isalpha()) or (a[i].isalpha() and a[i-1].isdigit()):
#              cur_len+=1
#          else:
#              max_len=max(cur_len,max_len)
#      print(max_len)


# В файле содержится последовательность натуральных чисел.
# Её элементы могут принимать целые значения от 1 до 100 000 включительно.
#
# Определите количество пар последовательности, в которых остаток от деления хотя бы одного из элементов
# на 16 равен минимальному элементу последовательности.
#
# Выведите на экран количество найденных пар, затем максимальную из сумм элементов таких пар.
#
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# with open("1700.txt", "r") as f:
#     data = list(map(int,f))
#     min_el = min(data)
#     answer = []
#     for i in range(len(data)-1):
#         z = data[i]
#         y = data[i+1]
#         if z % 16 == min_el or y % 16 == min_el:
#             answer.append(z + y)
#     print(len(answer), max(answer))




# with open("1710.txt", "r") as f:
#     data=list(map(int,f))
#     max_el=max(data)
#     answer=[]
#     k=0
#     for i in range(len(data)-1):
#         z=data[i]
#         y=data[i+1]
#         if (z+y)==max_el:
#             k+=1
#             answer.append(z**2+y**2)
#     print(k,max(answer))


# with open("1710.txt", "r") as f:
#     data=list(map(int,f))
#     max_el=max(data)
#     answer=[]
#     k=0
#     for i in range(len(data)-1):
#         z=data[i]
#         y=data[i+1]
#         if (z+y)==max_el:
#             k+=1
#             answer.append(z**2+y**2)
#     print(k,max(answer))


def func(x,l):
    return(10 <= x <= 99) ^ (10 <= l <= 99)
with open("1716.txt", "r") as f:
    data=list(map(int,f))
    min_el = 9999
    for i in data:
        if 10 <= i <= 99:
            if min_el > i:
                min_el = i
    answer = []
    for i in range(len(data)-1):
        z=data[i]
        y=data[i+1]
        if func(z,y) and (z+y) % min_el == 0:
            answer.append(z + y)
    print(len(answer), max(answer))

#



