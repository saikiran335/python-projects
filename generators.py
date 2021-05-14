def func(a):
    while a<=6:
        yield a
        a+=1
        
b=func(4)
next(b)

