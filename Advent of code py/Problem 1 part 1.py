# Code of advent first program

path = 'Sources\Input1.txt'

Advent_file = open(path,'r')
z = 0

Sample = Advent_file.readlines()
ConvSample = []

for element in Sample:

    ConvSample.append(element.strip())
    int(element)

for i, j in enumerate(ConvSample[:-1]):
    if j  < ConvSample[i+1]: 
        z += 1
z +=1

print(z)


# What we need is a program that compares the previous value with the new value and counts how many times the new value is bigger that the old value in the dataset
# The problem is that I don't know how to do that
# I think it could have something to do with for loops but who knows
# if previous value < new value, add one to z. The biggest problem I'm having is that I don't know how to define the values
# print z in the end