input = "Advent of code py\Sources\Input3.txt"

# Copied a part of this from Lagger

def part1(path):
    gamma = ''
    epsilon = ''
    List = []
    [List.append(x.strip()) for x in open(path,'r').readlines()]

    for x in range(12):
        zero = 0
        one = 0
        
        for y in List:
            
            if y[x] == '1':
                one += 1
            elif y[x] == '0':
                zero += 1
            else:
                raise ValueError('Invalid input!')
            
        if one > zero:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print('PART 1\n', 'power consuption:', int(gamma, 2) * int(epsilon, 2), '\n')

def part2(path):
    
    orn = []
    cosrn = []

    [orn.append(x.strip()) for x in open(path,'r').readlines()]
    [cosrn.append(x.strip()) for x in open(path,'r').readlines()]

    for x in range(12):
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
    for x in range(12):
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

    print('PART 2\n', 'life support rating:', int(orn[0], 2) * int(cosrn[0], 2), '\n')

part1(input)
part2(input)