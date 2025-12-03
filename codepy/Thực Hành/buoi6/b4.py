def bit_add(a, b):
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a
result = 0
a,b=map(int,input().split())
while b != 0:
    if b & 1:
        result = bit_add(result, a)
    a <<= 1
    b >>= 1
print(result)