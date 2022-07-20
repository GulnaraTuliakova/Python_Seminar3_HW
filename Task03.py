# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


n = input('Введите дробные числа через запятую(разделитель в числе - точка): ')
num = n.split(',')
list_d = []
for i in range(len(num)):
    a = float(num[i])
    b = round(a - int(a),2)
    list_d.append(b)
max = list_d[i] 
min = list_d[i] 
for i in range(len(list_d)):
    if list_d[i] > max:
        max = list_d[i]
    if list_d[i] < min:
        min = list_d[i]
print (f'Разница между максимальным и минимальным значением дробной части: {max} и {min} равно {round((max-min),2)}')
 

