# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


n = int(input('Введите целое число = '))
sum = 0
num = []
while n >= 1:
    sum = n - n//2*2
    n = n//2
    num.append(sum)
print('В двоичной системе: ', end='')
for i in range(len(num)):
    x = len(num)-i-1
    print(num[x], end='')

