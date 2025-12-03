def demuoc(n):
    tong=0
    for i in range(1,int(n**0.5+1)):
        if n%i==0:
            if i!=n//i:
                tong+=2
            else:
                tong+=1
    return tong 
n=int(input())
for i in range(1,n+1):
    if demuoc(i)==3:
        print(i,end=" ")