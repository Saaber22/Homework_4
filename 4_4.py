per = True
d = {'Head': 500, 'Body': 1000, 'Knife_left': 800, 'Shild':700,'Boots':300,'Trousers':900}
print('Инвентарь: ',d)
while per:
    s = 0
    for key,value in d.items():
        s += value
    print('Вес инвентаря:',s,'грамм')
    print('Макс. вес 5кг')
    maxs = 5000
    print('Список команд:\nДобавить - int\nУдалить - del\nВыход - exit')
    command = input('Введите команду:')
    if command == 'exit':
        per = False
    elif command == 'int':
        inv1 = input('Введите название предмета: ')
        inv2 = input('Введите его вес: ')
        if (s + int(inv2)) <= 5000:
            print('Места хватает в инвентаре')
            d.update({f'{inv1}':int(inv2)})
        else:
            print('Места недостаточно')
    elif command == 'del':
        dinv1 = input('Введите название предмета для удаления: ')
        if dinv1 in dict(d):
            print('Такой инвентарь есть, удаляем')
            d.pop(f'{dinv1}')
        else:
            print('Такого инвентаря нет')
    else:
        print('Команда введена неверно')
    print('Список инвентаря')
    for key,value in d.items():
        print(f'Название предмета: {key} - {value} грамм;')        
