path = 'Sources\Input2.txt'

Advent_file = open(path,'r')
Sample = Advent_file.readlines()
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

print('depth is: ', yval)
print('distance is: ', xval)
print('both multiplied is: ', xval * yval)