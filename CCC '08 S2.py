from sys import * 
import math
input = stdin.readline
radius = 10 
while radius != 0:
    radius = int(input())
    if radius!= 0:
        _sum = 0
        for y in range(1, radius):
            x = math.sqrt(radius * radius - y * y)
            _sum += math.floor(x) * 2 + 1 
        print(2 * _sum + 2 * radius + 3)