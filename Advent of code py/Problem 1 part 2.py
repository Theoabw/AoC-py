path = 'Sources\Input1.txt'

Advent_file = open(path,'r')
z = 0

Sample = Advent_file.readlines()
ConvSample = []
Newlist = []

for element in Sample:

    ConvSample.append(element.strip())


for i, j in enumerate(ConvSample[:-2]):
    Newlist.append(int(j) + int(ConvSample[i+1]) + int(ConvSample[i+2]))

for k, l in enumerate(Newlist[:-1]):
    if l  < Newlist[k+1]: 
        z += 1


print(z)

