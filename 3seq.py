input_numbers_1 = input('Введите номера 1-го списка: ')
input_numbers_2 = input('Введите номера 2-го списка: ')
if ',' in input_numbers_1:
    a = (',')
if '.' in input_numbers_1:
    a = ('.')
if '/' in input_numbers_1:
    a = ('/')
if ';' in input_numbers_1:
    a = (';')
if ' ' in input_numbers_1:
    a = (' ')
numbers_1 = list(input_numbers_1.split(a))
if ',' in input_numbers_2:
    a = (',')
if '.' in input_numbers_2:
    a = ('.')
if '/' in input_numbers_2:
    a = ('/')
if ';' in input_numbers_2:
    a = (';')
if ' ' in input_numbers_2:
    a = (' ')
numbers_2 = list(input_numbers_2.split(a))

#otvet = [i for i in numbers_1 if i not in numbers_2]
otvet = []
for i in numbers_1:
    if i not in numbers_2:
        otvet.append(i)

print(otvet)

