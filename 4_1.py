#Метод сортировки пузырьком
a=[10,6,8,2,4]
print(f'Список без сортировки: {a}')
l = int(len(a))
for i in range(l-1):
    for j in range(l-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a)
print(f'Отсортированный список: {a}')