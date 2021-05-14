import time
s=time.time()
t=time.ctime(s)
f=time.localtime()
a=time.asctime(f)
c=time.strftime("%m/%d/%Y")
d="13 May 2021"
e=time.strptime(d,"%d %B %Y")


print(s)
print(t)
print(f)
print(a)
print(c)
print(d)
print(e)
