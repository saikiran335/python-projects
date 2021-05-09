def linearsearch(a,n):
    for i in range(0,len(a)):
        if k==a[i]:
            break
            return (True,i)
            
        
        else:
            return False



n=int(input("enter size of array"))
a=[]
for i in range(0,n):
    a.append(int(input()))
k=int(input("enter number to saerch"))
linearsearch(a,n)
        
if(True):
    print("element found")
else:
    print("not found")
