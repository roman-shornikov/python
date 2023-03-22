# import math
# print("Введите число")
# a=int(input())
# z1 = math.cos(a)+math.sin(a)+math.cos(3*a)+math.sin(3*a)
# print("Первое значение")
# print(z1)
# z2 = 2*math.sqrt(2)*math.cos(a)*math.sin(math.pi/4+2*a)
# print("Второе значение")
# print(z2)

import math

a=-math.pi/4
b=math.pi/4
n=15

h=(b-a)/n
while a<b:
    F=math.sin(3*a)+4*a
    print(f"a={a} F={F}")
    a=a+h