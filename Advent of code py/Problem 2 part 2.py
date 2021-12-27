path = 'Sources\Input2.txt'

Advent_file = open(path,'r')
Sample = Advent_file.readlines()
xval = 0
yval = 0
aim = 0

for x in Sample:

    if 'down' in x:
        
        yn = int(x.strip('down '))
        aim += yn

    elif 'up' in x:
        
        yn = int(x.strip('up '))
        aim -= yn

    elif 'forward ' in x:
        
        xn = int(x.strip('forward '))
        xval += xn
        yval += aim * xn


print('depth is: ', yval)
print('distance is: ', xval)
print('both multiplied is: ', xval * yval)


