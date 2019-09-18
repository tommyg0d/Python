def f(x):
    if -2.4 <= x <= 5.7:
        return x*x
    else: return 4

num = input('Введите число: ')

if num:
    num = float(num)
    print(f(num))
else: print('Введите число!')
