'...TAn...Dung...NGuyen  '
s=input()
a=[]
dem=0
for i in range(len(s)):
    if s[i]!=' ':
        vt=i
        break
ss=s[vt::]
ss=ss+' '
x=""
for i in range(len(ss)):
    if ss[i]!=' ':
        x=x+ss[i]
        dem=dem+1
    if ss[i]==' ' and dem>0:
        a.append(x)
        x=""
        dem=0
print(len(a))
for x in a:
    print(x)