def fibon(n):
    if n>=3:

        return fibon(n-1)+fibon(n-2)
    else:
        return 1
n=int(input())
for i in range(1,n+1):
    if fibon(i)<=n:
        print(fibon(i),end=" ")
    else:
        break