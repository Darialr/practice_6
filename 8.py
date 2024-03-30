serial_num = int(input('Введите порядковый номер->'))

s = []

for i in range(0, 10):
    s.append(i)
for i in range(10, 100):
    s.append(i // 10)
    s.append(i % 10)
for i in range(100, 201):
    s.append(i // 100)
    s.append((i // 10) % 10)
    s.append(i % 10)

print(s[serial_num - 1])