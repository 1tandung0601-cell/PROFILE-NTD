def tonguoc(n):
    tong=0
    for i in range(1,int(n**0.5+1)):
        if n%i==0:
            if i!=n//i:
                tong+=i+n//i
            else:
                tong+=i
    return tong 
n=int(input())
if n==tonguoc(n)-n:
    print("YES")
else:
    print("NO")