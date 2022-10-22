#В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
#Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
#Ввод чисел продолжается до ввода пустой строки.
from functools import reduce
import math
import os
def clear(): return os.system('cls')


clear()

list = [int(i) for i in input('Введите числа через пробел: ').split()]
NOD = reduce(math.gcd, list)
print(NOD)
