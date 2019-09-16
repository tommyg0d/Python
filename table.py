atomNomer = input('Введите атомный номер элемента: ')

if atomNomer:
    atomNomer = int(atomNomer)
    if atomNomer == 3:
        print('Это Литий!')
    elif atomNomer == 25:
        print('Это Марганец!')
    elif atomNomer == 80:
        print('Это Ртуть!')
    elif atomNomer == 17:
        print('Это Хлор!')
    else: print('Не знаю, что это..')
else: print('Введите атомный номер элемента!')
