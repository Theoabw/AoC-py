with open('AoC\Sources\Input2.txt', 'r') as raw:
    Instr = [x.strip().split(' ') for x in raw.readlines()]
    Dir, val = [x[0] for x in Instr], [int(x[1]) for x in Instr]

def part1():
    
    xval = 0
    yval = 0

    for i, x in enumerate(Dir):

        if 'down' in x: yval += val[i]

        elif 'up' in x: yval -= val[i]

        else: xval += val[i]

    print(f"\nPart 1\nanswer is: {xval*yval}\n")

def part2():
    
    xval = 0
    yval = 0
    aim = 0

    for i, x in enumerate(Dir):

        if 'down' in x: aim += val[i]

        elif 'up' in x: aim -= val[i]

        else: 
            xval += val[i] 
            yval += aim * val[i]
    
    print(f"Part 2\nanswer is: {xval*yval}\n")

part1()
part2()