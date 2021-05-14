def fibonacci():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fibonacci():
    if x> 100:
        break
    print(x, end=" ")
    
