for i in range(1,15):
    if (100-7*i)%4==0:
        print("TRAU DUNG:",i,end=" ")
        print("TRAU NAM:",(100-7*i)//4,end=" ")
        print("TRAU GIA:",100-i-(100-7*i)//4)