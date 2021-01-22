import math


# accepts radius of circle and computes area

radius = float(input('Input the radius of the circle : '))
area = math.pi * radius * radius
print(f'The radius of the circle with radius {radius} is: {area}')


# accepts a filename and prints its extension

filename = input('Input the Filename: ')
f_extns = filename.split('.')
print ('The extension of the file is : ' + repr(f_extns[-1]))
