def check(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
n=int(input())
if n<4:
    print("Not Found 404")
else:
    for i in range(2,int(n**0.5)+1):
        if check(i) and i*i<=n:
            print(i*i,end=" ")