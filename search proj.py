def binarysearch(lst):
    n=int(input("enter the key to search:"))
    lst.sort()
    first=0
    last=len(lst)-1
    def binary(lst,n,first,last):
        mid=(first+(last-1))//2
        int(mid)
        if lst[mid] == n:
            print(n,"found at",mid)
        elif(n<lst[mid]):
            return binary(lst,n,first,mid-1)
        elif(n>lst[mid]):
            return binary(lst,n,mid+1,last)
    return binary(lst,n,first,last)

def linearsearch(lst,k):
    n=int(input("enter the key to search:"))
    for i in range(0,k):
        if(lst[i]== n):
            print(n, "found at:",i)
            break
        
            
        






print("--------Search strategies--------")
''' 1. binary search
    2. linear search
'''
b=int(input("enter tour choice:"))
k=int(input("enter the list size:"))
lst=[]
lst=list()
for i in range(0,k-1):
    f=int(input("enter values:"))
    lst.append(f)
if b == 1:
    print(binarysearch(lst))
elif b == 2:
    print(linearsearch(lst,k))
else:
    exit()
    

        
        
