path = "Advent of code py\Sources\Input1.txt"


def part1(path):
    
    List = []
    [List.append(x.strip()) for x in open(path, 'r').readlines()]
    [int(element) for element in List]

    z = 0

    for i, j in enumerate(List[:-1]):
        if j < List[i+1]:
            z += 1
    z += 1
    return z


def part2(path):

    List = []
    Newlist = []
    z = 0

    [List.append(x.strip()) for x in open(path, 'r').readlines()]

    for i, j in enumerate(List[:-2]):
        Newlist.append(int(j) + int(List[i+1]) + int(List[i+2]))

    for k, l in enumerate(Newlist[:-1]):
        if l < Newlist[k+1]:
            z += 1
    return z


print('Answer for part 1:', part1(path))
print('Answer for part 2:', part2(path))
