path = 'Sources\input4.txt'
Bingo = open(path,'r').readlines()
instruct = Bingo.pop(0)
Bingo.count('\n')

print()

class Bingoloc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

