from random import randint

def f(x):
    if x.index(max(x)) < x.index(min(x)):
        c = 0
        for j in range(x.index(max(x)), x.index(min(x))+1):
            if x[j] < 0:
                c += 1
    else:
        c = 1
        for j in range(x.index(max(x)), x.index(min(x)), -1):
            if x[j] < 0:
                c += 1
    return c

l = [randint(-1000, 1000) for i in range(1000)]
print(f(l))
