def isnub(s):
     try:
         nb = float(s)#The conversion of a string to a number is successfulTrue
         return True
     except ValueError as e:
         return False #Return to False if there is an exception
     return nb
s=input("Please enter the number:")
print("Check the format is correct!")
num=isnub(s)
print(num)