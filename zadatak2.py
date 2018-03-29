def kilometer_to_mile(kilometer):
    mile = 0.6213*kilometer
    return "%s mile" % mile
user=input("Please input kilometer: ")
num = float(user)
if num > 0:
    print("Data is ok")
else:
    print("Data is not ok")
    sys.exit()
num2=kilometer_to_mile(num)
print (num2)