def ucln(a,b):
    while b!=0:
        x=a%b
        a=b
        b=x
    return a
a,b=map(int,input().split())
print('UCLN= ',ucln(a,b))
print('BCNN= ',a*b//ucln(a,b))