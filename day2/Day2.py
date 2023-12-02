ans = 0
with open('test.txt', 'r') as file:
    file = file.read().strip()
    for line in file.split('\n'):
        ok = True
        id_, line = line.split(':')
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    ok = False

        if ok:
            ans += int(id_.split()[-1])

print(ans)
