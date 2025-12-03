from math import sqrt
a,b,c=map(int,input().split())
denta=b**2-4*a*c
if denta<0:
    print("PHUONG TRINH VO NGHIEM")
elif denta==0:
    print("PHUONG TRINH CO NGHIEM KEP")
    print("X1",-b/(2*a))
    print("X2",-b/(2*a))
else:
    print("PHUONG TRINH CO 2 NGHIEM PHAN BIET")
    print("X1=",(-b+sqrt(denta))/(2*a))
    print("X2=",(-b-sqrt(denta))/(2*a))