path = "Advent of code py\Sources\Input2.txt"

Sample = open(path,'r').readlines()

def printfunc(xval, yval):
    print('depth is:', yval)
    print('distance is:', xval)
    print('both multiplied is:', xval * yval, '\n')

def part1():
    
    xval = 0
    yval = 0

    for x in Sample:

        if 'down' in x:
            
            yn = int(x.strip('down '))
            yval += yn

        elif 'up' in x:
            
            yn = int(x.strip('up '))
            yval -= yn

        elif 'forward ' in x:
            
            xn = int(x.strip('forward '))
            xval += xn

    printfunc(xval, yval)

def part2():
    
    xval = 0
    yval = 0
    aim = 0

    for x in Sample:

        if 'down' in x:
            
            aim += int(x.strip('down '))

        elif 'up' in x:
            
            aim -= int(x.strip('up '))

        elif 'forward ' in x:
            
            xval += int(x.strip('forward '))
            yval += aim * int(x.strip('forward '))
    
    printfunc(xval, yval)

part1()
part2()