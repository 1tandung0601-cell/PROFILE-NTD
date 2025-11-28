n=int(input())
dem=1
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print(end="\n")
    for k in range(0,dem):
        print("  ",end="")
    dem+=1
    