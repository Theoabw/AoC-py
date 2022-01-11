path = 'Advent of code py\Sources\Input3.txt'

with open(path, 'r') as raw:
    List = raw.read().split('\n')
    Posval = []
    gamma = ''
    epsilon = ''

for pos in range(len(List[0])):
    Posval.extend([[0]])
        
    for byte in List:
        if byte[pos] == '1':
            Posval[pos][0] += 1

for bit in Posval:
    if bit[0] > int(len(List)/2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
        
print('answer: ', int(gamma, 2) * int(epsilon, 2))