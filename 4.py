cage = input('Введите клетку->').lower()
if ord(cage[0]) % 2 == int(cage[1]) % 2:
    print('черный')
else:
    print('белый')
