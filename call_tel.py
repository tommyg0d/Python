kod = input('Введите код города: ')
time = input('Введите длительность переговоров(мин): ')

kods = {
    343: 15,
    381: 18,
    473: 13,
    485: 11
}

if kod:
    
    if time:
        kod = int(kod)
        time = int(time)
        
        if kod in kods:
            print('Стоимость переговоров:',time*kods[kod],'руб.')
        else: print('Город не определён')
        
    else: print('Введите длительность переговоров!')
    
else: print('Введите код города!')
