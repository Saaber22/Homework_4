#Два случайных набора чисел
from random import randint

N = 10
#Инициализируем два списка
a = []
b = []
#Заполняем их рандомными числами
for i in range(N):
    a.append(randint(1,20))
    b.append(randint(1,20))
#Преобразуем их в множества
a = set(a)
b = set(b)
print('Множество a:',a)
print('Множество b:',b)
print('Входят одновременно в оба:',a.intersection(b))
print('Входят только в первое:',a.difference(b))
print('Входят только во второе:',b.difference(a))
print('Встречаются в одном, но не в обоих одновременно:',a.symmetric_difference(b))