raw = '''5212166716
1567322581
2268461548
3481561744
6248342248
6526667368
5627335775
8124511754
4614137683
4724561156
'''
raw = raw.splitlines()
raw = [[int(x) for x in row] for row in raw]
for r in raw:
     r.append("X")
     r.insert(0,"X")
temp = ["X"] * 12
raw.append(temp)
raw.insert(0, temp)

def doFlash(x,y,b):
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if b[i][j] != 'X' and b[i][j] != 0:
                b[i][j]+=1
                
def printBoard(b):
    for r in b:
        print(''.join(map(str,r)))
        
def allFlashed(b):
    count = 0
    for i in range(1,11):
        for j in range(1,11):
            if b[i][j] == 0:
                count+=1
    if count == 100:
        return True
    else:
        return False

flashes = 0
step = 0
allFlash = []

while step < 250: #set to 100 for part 1
    print(step)
    printBoard(raw)
    flashed = True
    for i in range(1,11):
        for j in range (1,11):
            raw[i][j]+=1
    #printBoard(raw)
    while flashed == True:
        flashed = False
        for i in range(1,11):
            for j in range (1,11):
                if raw[i][j] > 9:
                    doFlash(i,j,raw)
                    raw[i][j] = 0 
                    flashes+=1
                    flashed = True
    if allFlashed(raw) == True:
        allFlash.append(step+1)
    step+=1

print(flashes)
print(allFlash)
            
                
'''5212166716
1567322581
2268461548
3481561744
6248342248
6526667368
5627335775
8124511754
4614137683
4724561156
'''
    
            
