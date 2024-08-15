# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.
# STRINGS ARE IMMUTABLE WHICH MEANS THAT YOU CANNOT CHANGE THEM BY RUNNING FUNCTIONS ON THEM #IMP

a ='Tiger' # Single quoted string
b = "Zoe" # Double quoted string
c = '''Chotti''' # Triple quoted string

name = "rayyan" #The index in a string starts from 0 -> r to (length -1 -> n) in Python 
# Index Slicing -> name = [index_start:index_end] 

nameshort = name[0:3] #here we are asking the compiler to give only 0 to 3 letters of the name given (excluding 3)
print(nameshort) # The result we will get is ray [0 1 2] (excluding 3 which is 'y')

character1 = name[1] #return only letter 'a'
print(character1)