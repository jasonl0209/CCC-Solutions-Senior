from sys import *
n = int(stdin.readline())
d = int(stdin.readline())
if n%d == 0:
    print(n//d)
else:
    for i in range(1, min(n,d)+1):
        if max(n,d) % i == 0 and min(n,d) % i == 0:
            n = n//i
            d = d//i
    if n<d:
        print(str(n)+"/"+str(d))
    else:
        print(n//d, str(n%d)+"/"+str(d))
