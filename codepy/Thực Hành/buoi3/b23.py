def tonguoc(n):
    tong=0
    dem=0
    for i in range(1,int(n**0.5+1)):
        if n%i==0:
            if i!=n//i:
                tong+=i+n//i
                dem+=2
            else:
                tong+=i
                dem+=1
    return tong,dem
n=int(input())
t, d=tonguoc(n)
print("SO UOC:",d,"TONG UOC:",t)