steps, _, *rest = open("input.txt", "r").read().splitlines()

network = {}
for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1:-1].split(", ")

step_count = 0
curr = "AAA"

while curr != "ZZZ":
    step_count += 1
    curr = network[curr][0 if steps[0] == "L" else 1]
    steps = steps[1:] + steps[0]

print(step_count)
