from queue import LifoQueue



stack = LifoQueue()



def del_pos(number,position):
    return number[:position] + "_" + number[position + 1:]


b = int(input())
a = input()


"""

3
58889992


"""



"""DIT ME MAY BAT BO XEM SEG AN LON"""

for i in range( 0,len(a) - 1):

    
    num_1 = int(a[i])
    num_2 = int(a[i + 1])
    print(num_1,num_2)
    
    if(num_1 < num_2 and b > 0):
        a = del_pos(a,i)
        b -= 1
    

print(a)

