raw = [r.split(" -> ") for r in raw.splitlines()]
for row in raw:
    row[0] = [int(x) for x in row[0].split(',')]
    row[1] = [int(x) for x in row[1].split(',')]
grid = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    grid.append(row)
for row in raw:
    x1, y1, x2, y2 = row[0][0], row[0][1], row[1][0], row[1][1]
    if x1==x2 or y1==y2:
        if x1==x2:
            if y1>y2:
                y1,y2 = y2, y1
            for j in range(y1, y2+1):
                grid[x1][j]+=1
        else: #y1==y2
            if x1>x2:
                x1,x2 = x2, x1
            for i in range(x1, x2+1): #1,2;3,4 3,4;1,2
                grid[i][y1]+=1
    elif (x2 > x1 and y2 > y1) or (x1 > x2 and y1 > y2):
        if x1 > x2 and y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for i in range(x1,x2+1):
            for j in range(y1, y2+1):
                if i-x1 == j-y1:
                    grid[i][j]+=1
    elif x1>x2 and y1<y2: #6,2 2,6 (5,3; 4,4)
        for i in range(x1, x2-1, -1):
            for j in range(y1, y2+1):
                if x1-i == j-y1:
                    grid[i][j]+=1
    else: #x1<x2 and y1>y2
        for i in range(x1, x2+1):
            for j in range(y1, y2-1, -1):
                if i-x1 == y1-j:
                    grid[i][j]+=1
total = 0
for row in grid:
    for num in row:
        if num >=2:
            total+=1
print(total)
