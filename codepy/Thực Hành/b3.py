x=input()
t=""
for i in range(len(x)-1,-1,-1):
    t=t+x[i]
if t==x:
    print("la xau doi xung")
else:
    print("khong phai xau doi xung")