m, n = map(int, input().split())
a = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
b = []
for i in range(m):
    row = list(map(int, input().split()))
    b.append(row)
c = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(a[i][j] + b[i][j])
    c.append(row)
for row in c:
    print(*row)