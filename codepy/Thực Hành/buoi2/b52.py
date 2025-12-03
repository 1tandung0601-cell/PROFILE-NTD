n=int(input())
a=list(map(int,input().split()))
maxx=max(a)
F=[0]*(maxx+1)
for i in range(n):
    F[a[i]]=F[a[i]]+1
for i in range(maxx+1):
    if F[i]==1:
        print(i,end=" ")