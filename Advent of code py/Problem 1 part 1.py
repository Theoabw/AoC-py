path = 'Sources\Input1.txt'
List = []

def part1(path):
    
    [List.append(x.strip()) for x in open(path,'r').readlines()]
    [int(element) for element in List]

    z = 0

    for i, j in enumerate(List[:-1]):
        if j  < List[i+1]: 
            z += 1
    z += 1
    return z


print(part1(path))