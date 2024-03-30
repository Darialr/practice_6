a, b = map(int, input('Введите размер ковровой дорожки (через "x")->').split("x"))
if a**2 + b**2 <= (6.5*2)**2:
    print('да')
else:
    print('нет')
