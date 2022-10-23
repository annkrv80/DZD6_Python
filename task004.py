#Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.

from math import radians

n = int(input('Введите число n: '))
num = [i for i in range(1, n+1)]
res = sum(map(lambda i: (1+1/i)**i, num))
print(res)
