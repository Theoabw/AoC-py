path = 'Sources\input3.txt'

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
            raise Exception('Invalid input!')
    
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
            raise Exception('Invalid input!')
        
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

print('life support rating is:', int(orn[0], 2) * int(cosrn[0], 2))