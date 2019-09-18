def maxi(num1, num2):
    if num1 > num2:
        return num1
    else: return num2
    
a = input('Введите первое число: ')
b = input('Введите второе число: ')

if a and b:
    print(maxi(a,b))
else: print('Введите числа!')
