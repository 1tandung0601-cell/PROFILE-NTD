
def mu(a,b):
    kq=1
    for i in range(1,b+1):
        kq=kq*a
    return kq
def congbit(a,b):
    c=[]
    nho=0
    for i in range(len(a)-1,-1,-1):
        tong=a[i]+b[i]+nho
        if tong==0:
            c.append(0)
            nho=0
        elif tong==1:
            c.append(1)
            nho=0
        elif tong==2:
            c.append(0)
            nho=1
        else:
            c.append(1)
            nho=1
    if nho==1:
        c.append(1)
    return c
def bit(n):
    bt=[]
    while n>0:
        dv=n%2
        n=n//2
        bt.append(dv)
    bt.reverse()
    return bt
a=int(input())
b=int(input())
xau1=[]
xau2=[]
check=0
tong=0
if len(bit(a))<len(bit(b)):
    for i in range(len(bit(b))-len(bit(a))):
        xau1.append(0)
    check=1
if len(bit(b))<len(bit(a)):
    for i in range(len(bit(a))-len(bit(b))):
        xau1.append(0)
if check==0:
    xau1=xau1+bit(b)
    xau2=bit(a)
else :
    xau1=xau1+bit(a)
    xau2=bit(b)
kq=congbit(xau1,xau2)
for i in range(len(kq)):
    if kq[i]==1:
        tong=tong+mu(2,i)
print(tong)