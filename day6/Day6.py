import math

t, d = [list(map(int, line.split(":")[1].split())) for line in open("input.txt", "r")]

n = 1


for t, d in zip(t, d):
    m = 0
    for hold in range(t):
        if hold * (t - hold) > d:
            m += 1
    n *= m
print(n)



# for t, d in zip(t, d):
#     n *= math.floor((t + (t*t-4*d) ** 0.5) / 2) - math.floor((t - (t*t-4*d) ** 0.5) / 2)
#
# print(n)
