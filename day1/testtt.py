ans = 0
x = "1abc3"
fst = None
lst = None
for y in x:
    if y.isdigit():
        lst = y
        if fst is None:
            fst = y
ans += int(fst + lst)
print(ans)
