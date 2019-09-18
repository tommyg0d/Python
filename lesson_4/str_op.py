s = 'У лукоморья 123 дуб зеленый 123'

if s.index('я') != -1:
    print('Позиция "я" в строке: ',s.index('я'))
else: print('В строке нет "я"')

print('Буква "у" встречается',s.count('у'),'раз(а)')

if s.isalpha() == False:
    print(s.upper())

if len(s) > 4:
    print(s.lower())

print(s.replace(s[0],'О'))
    
