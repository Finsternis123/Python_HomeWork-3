#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = int(input('Enter numbers 1 to 5: '))
# c = int(input('Enter numbers 1 to 5: '))
# number = 0
# n += 1
# list = []
# for i in range(1, n):
#     list.append(i)
#     if i == c:
#         number += 1
# print(list)
# print(number)

# Пытался написать через генератор рандомных чисел, но не понимаю как продолжить считать после первого прохода цикла... более того, почему увеличивается список. Надо разобраться.
import random as r
n = int(input('Enter number: '))
c = int(input('Enter number: '))
counter = 0
n += 1
list = []
for i in range(1, n):
    a = r.randint(1, 5)
    list.append(a)
    if a == c:
        counter += 1
print(list)
print(counter)