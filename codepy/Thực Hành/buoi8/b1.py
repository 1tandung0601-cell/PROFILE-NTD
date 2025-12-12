a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("tam gia deu")
    elif a==b or b==c or a==c:
        print("tam gia can")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("tam giac vuong")
    else:
        print("tam giac thuong")