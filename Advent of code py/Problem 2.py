path = 'Sources\Input2.txt'

Advent_file = open(path,'r')
Sample = Advent_file.readlines()
ConvSample = []
downlist = []
uplist = []
fwlist = []
xval = 0
yval = 0

for element in Sample:

    ConvSample.append(element.strip())

for x in ConvSample:
   if 'down' in x:
       downlist.append(x)
   elif 'up' in x:
       uplist.append(x)
   elif 'forward' in x:
       fwlist.append(x)

downval = []
upval = []
fwval = []

for term in downlist:

    downval.append(term.strip('down '))

for term in uplist:

    upval.append(term.strip('up '))

for term in fwlist:

    fwval.append(term.strip('forward '))

# for loops go brrrrrrr

for down in downval:
    yval += int(down)

for up in upval:
    yval -= int(up)

for forward in fwval:
    xval += int(forward)

print('depth is: ', yval)
print('distance is: ', xval)
print('both multiplied is: ', xval * yval)