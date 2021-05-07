import random
from sympy import *
print("""----------------Guess me----------------""")


hint=""
score=0
t=5
while(t>0):
    n=random.randint(0,10)
    if(n%2==0):
        hint="--it may be an even number--"
    elif(isprime(n)):
        hint="--it may be a prime number--"
    elif(n%5==0):
        hint="--it may be a end with '0' or '5'--"
    elif(n%2!=0):
        hint="--it may be an odd number--"
    else:
        hint="--it may be a natural number--"
    print("\n\nHINT------->",hint)
        
    print("\n\nenter your chouce")
    a=int(input())
    if(a>100):
        print("\n\nenter number between 0 and 10")
    else:
        if(a==n):
            score=score+10
            print("\nCorrect")
        else:
            score=score-5
            print("\nWrong")
    t=t-1
print("\n\nyou have completed your turns")
print("\n\nyour score is",score)
        
    
