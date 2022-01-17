with open('AoC\Sources\Input4.txt', 'r') as raw:
    read = raw.read().split('\n\n')
    numbers = tuple([int(x) for x in read[0].split(',')])
    boards = [[[int(num) for num in line.split()] for line in board.split('\n')] for board in read[2:]]

def bview(board):
        print('Board', boards.index(board) + 1, '\n')
        for row in board:
            print(row)
        print('\n')
        return boards.index(board) + 1

def Marker(num, board):
    for row in board:
        for pos in range(len(row)):
            if row[pos] == num:
                row[pos] = 'x'

def wincheck(board):
    Win = False
    for row in board:
        if all(nums in ['x'] for nums in row):
            Win = True
        if Win:
            return Win
    for x in range(len(board)):
        col = []
        for row in board:
            col.extend([row[x]])
        for row in board:
            if all(nums in ['x'] for nums in col):
                Win = True
            if Win:
                return Win
    return Win

def sum(board):
    sum = 0
    for row in board:
        for num in row:
            if num != 'x':
                sum += num
    return sum

# def part1():
#     bcopy = boards
#     numcopy = numbers
#     count = 0
#     for num in numcopy:
#         count += 1
#         for board in bcopy:
#             Marker(num, board)
#             if wincheck(board):
#                 bview(board)
#                 print('at count', count)
#                 return sum(board) * num
# print('part 1 answer:', part1())

def part2():
    bcopy = boards
    numcopy = numbers
    bcount = len(bcopy)
    for num in numcopy:
        for board in bcopy:
            Marker(num, board)
            if wincheck(board):
                print('removing board', bview(board))
                bcopy.remove(board)
        if len(bcopy) < 2 and not wincheck(bcopy[0]):
                for board in bcopy:
                    Marker(num, board)
                    if wincheck(board):
                        return (sum(board) * num)
                
                


print(part2())

# 36975 control