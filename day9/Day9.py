def thing(l):
    if all(x == 0 for x in l):
        return 0
    deltas = [l[i + 1] - l[i] for i in range(len(l) - 1)]
    diff = thing(deltas)
    # return l[-1] + diff
    return l[0] - diff


total = 0

for line in open("input.txt"):
    nums = list(map(int, line.split()))
    total += thing(nums)

print(total)
