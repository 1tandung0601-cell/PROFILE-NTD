h,p,s=map(int,input().split())
if 0<=p+1<60:
    p+=1
else:
    p=0
    if 0<=h+1<=23:
        h+=1
    else:
        h=0
print(h,p,s)