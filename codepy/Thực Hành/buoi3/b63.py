n=int(input())
F=[0]*(10**6)
F[1]=F[2]=1
i=3
while True:
    F[i]=F[i-1]+F[i-2]
    if F[i]>n:
        break
    i+=1
for j in range(1,i):
    print(F[j],end=" ")