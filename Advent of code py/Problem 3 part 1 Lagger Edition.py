path = 'Sources\Input3.txt'

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
            raise Exception('Invalid input!')
        
    if one > zero:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'


print('gamma is:', gamma)
print('epsilon is:', epsilon, '\n')

print('power consuption is:', int(gamma, 2) * int(epsilon, 2))