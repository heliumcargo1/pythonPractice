import math

def circle(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area,circumference

r1,r2 = circle(2)

print(round(r1,2),round(r2,2))