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

[downval.append(x.strip('down ')) for x in downlist]
[upval.append(x.strip('up ')) for x in uplist]
[fwval.append(x.strip('forward ')) for x in fwlist]

downval = [int(x) for x in downval]
upval = [int(x) for x in upval]
fwval = [int(x) for x in fwval]

# for loops go brrrrrrr

for down in downval:
    yval += down

for up in upval:
    yval -= up

for forward in fwval:
    xval += forward

print('depth is: ', yval)
print('distance is: ', xval)
print('both multiplied is: ', xval * yval)