from operator import index


with open('AoC\Sources\Input5.txt', 'r') as raw:
    List = [[[int(num) for num in coord.split(',')] for coord in x.strip('\n').split(' -> ')] for x in raw.readlines()]
    xy = []
    graph = []


def printfunc(input):
    x=0
    for line in input:
        print('index', x , ':' , line)
        x += 1
    


def xycheck():
    
    for line in List:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            xy.append(line)


xycheck()
printfunc(xy)



