def mu(n,k):
    x=n
    n=1
    if k==0:
        return 1
    for i in range(k):
        n=n*x
    return n
n=int(input())
k=1
dem=0
while mu(5,k)<=n:
    dem+=n//mu(5,k)
    k+=1
print(dem)
