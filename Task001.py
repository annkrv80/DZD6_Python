#В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
#Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
#Ввод чисел продолжается до ввода пустой строки.
from functools import reduce
import math
import numbers
import os
def clear(): return os.system('cls')


clear()

numbers = []
while (True):
    i = input('Введите число: ').strip()
    if i == '':
        break
    numbers.append(i)
sp = list(map(int, numbers))
NOD = reduce(math.gcd, sp)
print(NOD)
