#This a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

try :
    var

except NameError as err :
    print(err)
    print("Tryna don't initialise empty variable in the future, for now we are just assigning the value None to your variable 'var', Thanks !")
    var = None

finally :
    print("The value for var is:", var)
