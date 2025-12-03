
m,n= map(int,input().split())



"""
a=list(map(int,input().split()) for _ in range(m))
b=list(map(int,input().split()) for _ in range(m))
for i in range(m):
    for j in range(n):
        a[i][j]+=b[i][j]
print(*a)"""

a = []
for _ in range(m):
    temp = [list(map(int, input().split())) for _ in range(n)]
    a.append(temp)
print(a)

