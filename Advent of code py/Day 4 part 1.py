path = "Advent of code py\Sources\Input4.txt"
with open(path, 'r') as raw:
    numbers, *boards = raw.read().split("\n\n")
    numbers = [int(i) for i in numbers.split(',')]
    AllBoards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]
    
    # for board in boards:
    #     for row in board.split('\n'):
    #         for col in row.split():
    #             int(col) 

def Boardview():
    for board in AllBoards:
        for col in board:
            print(col)
        print('\n')

# Boardview()
# print(boards)

def Marker(number, board):
    for row in board:
        for num in range(len(row)):
            if row[num] == number:
                row[num] = 'x'

def Wincheck(board):
    Win = False
    for x in range(len(board)):
        count = 0
        for row in board:
            if row[x] == 'x':
                count += 1
        if count == len(board):
            Win = True
        else:
            for row in board:
                count = 0
                for num in row:
                    if num == 'x':
                        count += 1
                if count == len(row):
                    Win = True
                    print('Win')
    
    return Win

def Sum(board):
    sum = 0
    for row in board:
        for num in row:
            if num != 'x':
                sum += num
    return sum


            
Marker(14, AllBoards[0])
Marker(33, AllBoards[0])
Marker(79, AllBoards[0])
Marker(61, AllBoards[0])
Marker(44, AllBoards[0])

def part1():
    for num in numbers:
        for board in AllBoards:
            Marker(num, board)
            if Wincheck(board):
                return Sum(board) * num
            
print(part1())
# wrong answer