a, b = map(int, input('Введите размер отверстия (Длина x Ширина")').split())
c, d, e = map(int, input('Введите размер кирпичей (Длина x Ширина х Высота")').split())
if a >= c and (b >= e or b >= d):
    print('да')