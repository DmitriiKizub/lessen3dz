input_string = input('Введите элементы списка через запятую (точку с запятой или слэш) : ')
if ',' in input_string:
    a = (',')
if '.' in input_string:
    a = ('.')
if '/' in input_string:
    a = ('/')
if ';' in input_string:
    a = (';')
vals = input_string.split(a)
def get_numers(vals):
    ver = []
    ver_ds = set(vals)

    for vals in ver_ds:
        ver.append(vals)
    return ver
print(get_numers(vals))