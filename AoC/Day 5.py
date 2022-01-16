with open('AoC\Sources\Input5.txt', 'r') as raw:
    List = [[[int(num) for num in coord.split(',')] for coord in x.strip('\n').split(' -> ')] for x in raw.readlines()]
    xy = []
    grid = []

def printfunc(input):
    for line in input:
        print('index', input.index(line) , ':' , line)

def xycheck():
    
    for line in List:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            xy.append(line)

def mkgrid():
    for line in range(1000):
            grid.extend([[]])
            y = 0
            while y < 1000:
                grid[line].append(0)
                y += 1

def linedraw():
    for line in xy:
        xindex = 0
        yindex = 0
        x1, x2 = line[0][0], line[1][0] 
        y1, y2 = line[0][1], line[1][1]

        if x1 == x2:
            
            xindex = x1
            # order check
            if y1 > y2:
                mark = [num for num in range(y2, y1 + 1)]
            else:
                mark = [num for num in range(y1, y2 + 1)]

        elif y1 == y2:
            yindex = y1
            # order check
            if line[0][0] > line[1][0]:
                mark = [num for num in range(x2, x1 + 1)]
            else:
                mark = [num for num in range(x1, x2 + 1)]

        else:
            print('something went wrong')

        # for pos in mark:
        #     if xindex:
        #         grid[pos].insert(grid[pos][xindex] + 1, xindex)
        #     elif yindex:
        #         grid[yindex].insert(grid[yindex][pos] + 1, pos)
        for pos in mark:
            if xindex:
                grid[pos][xindex] += 1
            elif yindex:
                grid[yindex][pos] += 1

def sumcheck():
    sum = 0
    check = []
    for line in grid:
        check.extend([[]])
        for pos in line:
            if pos > 1:
                sum += 1
    return sum

def part1():
    xycheck()
    mkgrid()
    linedraw()
    print('\npart 1')
    print('Answer is:', sumcheck(), '\n')

# I might be overusing functions

part1()