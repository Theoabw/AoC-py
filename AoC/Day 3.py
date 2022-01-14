path = 'AoC\Sources\Input3.txt'

with open(path, 'r') as raw:
    List = raw.read().split('\n')
    Posval = []

def part1():

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
    
    print('\nPART 1')
    print('power consumption: ', int(gamma, 2) * int(epsilon, 2))

def part2():
    
    orn = []
    cosrn = []

    [orn.append(x.strip()) for x in open(path,'r').readlines()]
    [cosrn.append(x.strip()) for x in open(path,'r').readlines()]

    for x in range(len(orn[0])):
        zero = 0
        one = 0
        
        for y in orn:
            
            if y[x] == '1':
                one += 1
            elif y[x] == '0':
                zero += 1
            else:
                raise ValueError('Invalid input!')
        
        # Numbers to keep
        if one >= zero:
            nkeep = '1'
        else:
            nkeep = '0'

        for y in orn:
            if y[x] != nkeep:
                orn = list(filter((y).__ne__, orn))

        if len(orn) == 1:
            break

    #---------------
    for x in range(len(cosrn[0])):
        zero = 0
        one = 0

        for y in cosrn:
            
            if y[x] == '1':
                one += 1
            elif y[x] == '0':
                zero += 1
            else:
                raise ValueError('Invalid input!')
            
        # Numbers to keep
        if one >= zero:
            nkeep = '0'
        else:
            nkeep = '1'

        for y in cosrn:
            if y[x] != nkeep:
                cosrn = list(filter((y).__ne__, cosrn))
            
        
        if len(cosrn) == 1:
            break

    print('\nPART 2')
    print('life support rating:', int(orn[0], 2) * int(cosrn[0], 2), '\n')


part1()
part2()