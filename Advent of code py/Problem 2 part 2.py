path = 'Sources\Input2.txt'

Sample = open(path,'r').readlines()
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


print('depth is: ', yval)
print('distance is: ', xval)
print('both multiplied is: ', xval * yval)