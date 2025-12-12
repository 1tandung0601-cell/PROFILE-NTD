import sys
sys.stdin = open("test.inp", "r")
sys.stdout = open("test.out", "w")
a, b = map(int, input().split())
print(a+b)