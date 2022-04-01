input_string = input('Введите элементы списка через запятую (точку с запятой или слэш) : ')
if ',' in input_string:
    a = (',')
if '.' in input_string:
    a = ('.')
if '/' in input_string:
    a = ('/')
if ';' in input_string:
    a = (';')
if ' ' in input_string:
    a = (' ')
vals = set(input_string.split(a))
print('Результат:', list(vals))

#def get_numers(vals):
   # ver = []
 #   print(vals)
  #  for vals in vals:
   #     ver.append(vals)
        #return ver
#get_numers(vals)
