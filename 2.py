a, b = map(int, input('Введите размер отверстия (Длина x Ширина")->').split('x'))
c, d, e = map(int, input('Введите размер кирпичей (Длина x Ширина х Высота")->').split('x'))
if a >= c and b >= d:
    print('да')
if a >= d and b >= c:
    print('да')
if a >= c and b >= e:
    print('да')
if a >= e and b >= c:
    print('да')
if a >= d and b >= e:
    print('да')
if a >= e and b >= d:
    print('да')
else:
    print('нет')
