
def add(a, b): #더하기
    return a+b

def sub(a, b): #빼기
     return a-b
 
def mul(a, b): #곱하기
     return a * b
 
def dev(a, b):  #나누기
     return a/b
 
def abs(a):  #양수,음수
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
