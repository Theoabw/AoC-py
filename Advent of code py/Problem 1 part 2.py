path = 'Sources\Input1.txt'

List = []
Newlist = []

def part2(path):
    z = 0
    [List.append(x.strip()) for x in open(path,'r').readlines()]

    for i, j in enumerate(List[:-2]):
        Newlist.append(int(j) + int(List[i+1]) + int(List[i+2]))

    for k, l in enumerate(Newlist[:-1]):
        if l  < Newlist[k+1]: 
            z += 1
    return z


print(part2(path))

