x=input()
n=int(input())
c=ord(x)
if c>=65 and c<=90:
    if c+n>90:
        t=(c+n)-90
        vt=t%25
        print(chr(64+vt))
    else :
        print(chr(c+n))

