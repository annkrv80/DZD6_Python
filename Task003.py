#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from itertools import count
from random import randint

sp = [randint(0, 10) for i in range(6)]
print(sp)
res = filter(lambda r: sp.count(r) == 1, sp)
print(list(res))
