# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = int(input('Введите число n чисел, которые необходио добавить в список: '))

num = list(range(1, n*3, 3))
print (num)
sum = 0
for i in range(len(num)):
    if i % 2 == 0:
        sum = sum + num[i]
print(f'Сумма чисел на нечетных позициях = {sum}')
  
