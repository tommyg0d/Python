kod = input('Введите код города: ')
time = input('Введите длительность переговоров(мин): ')

price = 0

if kod:
    kod = int(kod)
    if time:
        time = int(time)
        if kod == 343:
            price = 15 * time
        elif kod == 381:
            price = 18 * time
        elif kod == 473:
            price = 13 * time
        elif kod == 485:
            price = 11 * time
        else: print('Город не определён')
        print('Стоимость переговоров:',price,'руб.')
    else: print('Введите длительность переговоров!')
else: print('Введите код города!')
