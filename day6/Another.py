import math

t, d = [int("".join(line.split(":")[1].split())) for line in open("test.txt", "r")]
a = 1
b = -t
c = d
x1 = (-b - (b*b-4*a*c) ** 0.5) / 2 * a
x2 = (-b + (b*b-4*a*c) ** 0.5) / 2 * a

print(math.floor(x2) - math.ceil(x1))

