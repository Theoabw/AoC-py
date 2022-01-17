from re import L


with open('AoC\Sources\Input5.txt', 'r') as raw:
    List = raw.readlines()


for line in List:
    point1, point2 = line.split('->')
    x1, y1 = tuple(map(int, point1.split(',')))
    x2, y2 = tuple(map(int, point2.split(',')))

    # if x1 == x2 or y1 == y2:
        
