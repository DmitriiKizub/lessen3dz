elements = int(input('Введите кол-во элементов: '))
elements_ch = range(1,elements+1)
cifra_a=list()
for i in elements_ch:
    cifra = input(f"Введите {i} элемент: ")
    cifra_a.append(cifra)
cifra_a.sort()
cifra_a
print(f'Вывод :{cifra_a}')
