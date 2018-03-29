import math
def cubevolume(length,width,height):
    try:
        l = float(length)
        w = float(width)
        h = float(height)
    except ValueError as e:
        return False
    volume=l*w*h
    return volume
#test code
length=input("Please enter the length of the cube: ")
height=input("Please enter the height of the cube: ")
width=input("Please enter the width of the cube: ")
volume1=cubevolume(length,width,height)
print("The volume of the cube is")
print(volume1)