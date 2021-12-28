
def add(a, b):
    return a+b

def sub(a, b):
     return a-b
 
def mul(a, b):
     return a * b
 
def dev(a, b):
     return a/b
 
def abs(a):
    if a > 0 :
        return a
    else :
        return - a

a=10
b=10
c=add(a,b)
d=sub(a,b)
e=mul(a,b)
f=dev(a,b)
h=abs(a)
print(c,d,e,f,h)
