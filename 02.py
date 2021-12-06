raw = raw.splitlines()
x,y = 0,0
for r in raw:
    r = r.split(" ")
    amt = int(r[1])
    if r[0] == "forward":
        x += amt
    elif r[0] == 'up':
        y -= amt
    else:
        y += amt
print(x*y)
x,y,aim = 0,0,0
for r in raw:
    r = r.split(" ")
    amt = int(r[1])
    if r[0] == "forward":
        x += amt
        y += amt * aim
    elif r[0] == 'up':
        aim -= amt
    else:
        aim += amt
print(x*y)