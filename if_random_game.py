import random

num = random.randint(1, 4)
a = input('Загадайте число от 1 до 4: ')

if a:
    a = int(a)
    if a == num:
        print('Победа!')
    else:
        if a > num:
            print('Число было меньше')
        else: print('Число было больше')
        print('Повторите еще раз')
else: print('Загадайте число!')
