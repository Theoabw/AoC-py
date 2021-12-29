path = 'Sources\Input3.txt'

Advent_file = open(path,'r')
Sample = Advent_file.readlines()
List = []
gamma = ''
epsilon = ''
pos1 = []
pos2 = []
pos3 = []
pos4 = []
pos5 = []
pos6 = []
pos7 = []
pos8 = []
pos9 = []
pos10 = []
pos11 = []
pos12 = []
stramount = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
intamount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

[List.append(x.strip()) for x in Sample]

for x in List:
    pos1.append(x[0])
    pos2.append(x[1])
    pos3.append(x[2])
    pos4.append(x[3])
    pos5.append(x[4])
    pos6.append(x[5])
    pos7.append(x[6])
    pos8.append(x[7])
    pos9.append(x[8])
    pos10.append(x[9])
    pos11.append(x[10])
    pos12.append(x[11])

if pos1.count('1') > pos1.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos2.count('1') > pos2.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos3.count('1') > pos3.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos4.count('1') > pos1.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos5.count('1') > pos5.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos6.count('1') > pos6.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos7.count('1') > pos7.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos8.count('1') > pos8.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos9.count('1') > pos9.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos10.count('1') > pos10.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos11.count('1') > pos11.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'

if pos12.count('1') > pos12.count('0'):
    gamma += '1'
    epsilon += '0'
else:
    gamma += '0'
    epsilon += '1'


# I know I'm pretty retarded

print(int(gamma, 2)*int(epsilon, 2))