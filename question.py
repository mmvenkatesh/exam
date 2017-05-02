import math
x=[1,3,4,4]
y=[2,5,5,3]
n=len(x)

def exp1(x,y):
    c=0
    for a,b in zip(x,y):
        c=c+(a*b)
    return c

def exp2(f):
    d=0
    for a in f:
        d=d+a
    return d
    
def exp3(f):
    e=0
    for a in f:
        e=e+(a*a)
    return e    

value1=exp1(x,y)-(exp2(x)*exp2(y))/n
value2=exp3(x)-(exp2(x)**2)/n
value3=exp3(y)-(exp2(y)**2)/n

r=value1/math.sqrt(value2*value3)

print r
