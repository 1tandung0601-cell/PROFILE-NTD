s=input()
T=True
for i in range(len(s)):
    if(s[i]!=" " and T==True):
        print(s[i].upper(),end="")
        T=False
    elif s[i]!=" " and T==False:
        print(s[i].lower(),end="")  