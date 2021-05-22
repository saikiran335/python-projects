import random
def dice(c):
    
    while c == "1":
        r=input("\nTo Roll Dice press R (or) r")
        if r=="R" or r=="r":
            i=random.randint(1,6)
            if i > 4 :
                c="1"
                
                print(i)
                print(dice(c),end= " ")
                break
            else:
                print(i)
                break
        break
                
c=input("press num '1' ")    
dice(c)
 
