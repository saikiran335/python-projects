a=0
b=1
n=int(input("enter number"))
print(a)
for i in range(0,n):
    
    a,b=b,a+b
    if a<n:
        print(a, end="")
