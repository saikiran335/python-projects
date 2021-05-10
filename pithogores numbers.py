from math import sqrt
n=int(input())
for a in range(1,n+1):
    for b in range(a,n):
        c_squere=a**2 + b**2
        c=int(sqrt(c_squere))
        if((c_squere - c**2)==0):
            print(a,b,c)
