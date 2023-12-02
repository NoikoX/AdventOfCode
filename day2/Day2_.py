answer = 0
for i, x in enumerate(open('D:\AdventOfCodePy\day2\input2.txt', 'r')):
    gs = x.strip().split(': ')[1].split('; ')
    for g in gs:
        m = {"red": 0, "green": 0, "blue": 0}
        for e in g.split(', '):
            a, b = e.split()
            m[b] = int(a)
        if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14:
            break
    else:
        answer += i + 1
print(answer)

# Part 2

answer = 0
for i, x in enumerate(open('D:\AdventOfCodePy\day2\input2.txt', 'r')):
    gs = x.strip().split(': ')[1].split('; ')
    tm = {"red": 0, "green": 0, "blue": 0}

    for g in gs:
        m = {"red": 0, "green": 0, "blue": 0}
        for e in g.split(', '):
            a, b = e.split()
            m[b] = int(a)
        for k in tm:
            tm[k] = max(tm[k], m[k])
    answer += tm["red"] * tm["green"] * tm["blue"]

print(answer)