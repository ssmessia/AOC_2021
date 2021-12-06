import copy
def getBoards(s):
    s = s.splitlines()
    boards = []
    board = []
    for i in range(len(s)):
        if s[i] == '':
            boards.append(board)
            board = []
        else:
            board.append([int(x) for x in s[i].split()])
    return boards

def changeBoards(x, b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            for k in range(5):
                if b[i][j][k] == x:
                    b[i][j][k] = "*"

def checkBoards(b):
    winners = []
    for k in range(len(b)):
        win = 0
        for row in b[k]:
            if len(set(row)) == 1:
                win = 1
        for j in range(5):
            count = 0
            for i in range(5):
                if b[k][i][j] == '*':
                    count+=1
            if count == 5:
                win = 1
        if win == 1:
            winners.append(k)
    return winners
           
boards = getBoards(b)
for i in range(len(nums)):
    changeBoards(nums[i], boards)
    winners = checkBoards(boards)
    if len(winners) == 1:
        total = 0
        for row in boards[winners[0]]:
            for num in row:
                if num != '*':
                    total+=num
        print(total*nums[i])
    elif len(winners) == 100:
        print("All boards have won")
        total = 0
        last = list(set(winners) - set(oldwinners))
        print(last)
        for row in boards[last[0]]:
            for num in row:
                if num != '*':
                    total+=num
        print(total*nums[i])
        break
    oldwinners = copy.deepcopy(winners)