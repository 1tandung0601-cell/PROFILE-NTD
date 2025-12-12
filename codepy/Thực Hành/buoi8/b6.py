n=int(input())
cs=0
while n>0:
    cs+=1
    n=n//10
if cs%3==0:
    print(cs//3-1)
else:
    print(cs//3)