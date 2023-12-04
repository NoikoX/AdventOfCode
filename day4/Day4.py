mapunia = {}
for i, x in enumerate(open("input.txt", "r")):
    if i not in mapunia:
        mapunia[i] = 1
    x = x.split(":")[1].strip()
    a, b = [list(map(int, k.split())) for k in x.split(" | ")]
    n = sum(p in a for p in b)

    for k in range(i + 1, i + n + 1):
        mapunia[k] = mapunia.get(k, 1) + mapunia[i]


print(sum(mapunia.values()))


