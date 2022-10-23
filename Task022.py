#Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
#Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
#Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек
import os
def clear(): return os.system('cls')


clear()

data = input('Введите текст: ')
count = 0
ch = 'Р'
res = []
for i in range(len(data)):
    if data[i] == ch:
        count += 1
    else:
        res.append(count)
        count = 0
    if data[-1] == ch:
        res.append(count)
print(max(res))
