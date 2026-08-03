def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>a and b>c):
        return a
    elif(c>b and c>a):
        return c
a=1
b=3
c=4
print(greatest(a,b,c))