# ans = 0
# with open("input.txt", "r") as file:
#     fst = None
#     lst = None
#     for y in file.read():
#         if y.isdigit():
#             lst = y
#             if fst is None:
#                 fst = y
#     ans += int(fst + lst)
#     print(ans)


ans = 0
with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        fst = None
        lst = None
        for y in line:
            if y.isdigit():
                lst = y
                if fst is None:
                    fst = y
        ans += int(fst + lst)

print(ans)