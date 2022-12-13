#Словарь цветов
print('Словарь цветов')
d = {'red': (255, 0, 0), 'yellow': (255,255,0), 'green': (0,255,0), 'blue':(0,0,255),'white':(255,255,255),'black':(0,0,0)}
print(dict.keys(d))
for key,value in d.items():
    print(f'{key}: {value};')
