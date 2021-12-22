raw = 'target area: x=287..309, y=-76..-48'
test = 'target area: x=20..30, y=-10..-5'
#raw = test
raw = raw.split(': ')
raw[1] = raw[1].split(', ')
for r in raw[1]:
    if r[0] == 'x':
        r = r.split('=')
        r[1] = r[1].split('..')
        min_x = int(r[1][0])
        max_x = int(r[1][1])
    else:
        r = r.split('=')
        r[1] = r[1].split('..')
        min_y = int(r[1][0])
        max_y = int(r[1][1])

print(min_x, max_x, min_y, max_y)

def getStep(x, y, x_vel, y_vel):
    x+=x_vel
    y+=y_vel
    if x_vel > 0:
        x_vel-=1 
    y_vel-=1
    return([x, y, x_vel, y_vel])
    
def getSteps(x,y,x_vel,y_vel,min_y):
    steps = []
    while y >= min_y:
        x+=x_vel
        y+=y_vel
        if x_vel > 0:
            x_vel-=1 
        y_vel-=1
        steps.append([x,y])
    return(steps)

def checkSteps(steps, min_x, max_x, min_y, max_y):
    for s in steps:
        if min_x <= s[0] <= max_x and min_y <= s[1] <= max_y:
            return True
    return False


best_x, best_y = 0,0
highest = 0
good_values = []
for i in range(500):
    for j in range(-400,400):
        steps = getSteps(0,0,i,j,min_y)
        if checkSteps(steps, min_x, max_x, min_y, max_y) == True:
            good_values.append([i,j])
            if max([r[1] for r in steps]) > highest:
                best_x, best_y, highest = i,j, max([r[1] for r in steps])

print(highest)
print(len(good_values))

