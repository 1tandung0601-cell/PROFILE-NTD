a=int(input())
n=input()
h=n
c=len(h)
def so(i,a,n):
    b=i
    for e in range(i+1,a+1):
        if int(n[b])<int(n[e]):
            b=e
        if int(n[b])==9:
            break
    n=n[i:b+1]
    return n
i=0
while c-a>len(n):
    n=so(i,a,n)
    i=i+1
    a=a-1
print(n)


