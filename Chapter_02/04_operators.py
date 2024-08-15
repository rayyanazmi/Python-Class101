# Operators in python 
'''
Following are some common operators in python:
1. Arithematic operators: +, -, *, / etc
2. Assignment operators: =, +=, -= etc
3. Comparison Operators: ==, >, >=, <, <=, != etc
4. Logical operators: and, or, not.'''

# Arthematic operator (7+4 = 11) 
'''where '7' and '4' are operands
and '+' is an operator
lastly '11' is the result'''

a = 10

b = 5

c = a + b
print(c)

# Assignment Operators (to put value in a variable we use =)

a = 8-2 #Assign 8-2 in a
print(a)
b = 6
# b += 3 #Increment the value of b by 3 and then assign it to b
b -=4 #Decrement the value of b by 4 and then assign it to b
print(b)

# Comparison operator (to check that the values are equal to each other or not then we use ==)

x = 5==5 
print(x)

# Logical operators 

z = True or False

#Truth table of 'or' --- if one value is true it will print true else false (KANOON)
print("This is the truth table of or")
print("True or False is", True or False)
print("True and True is", True or True)
print("False and True is", False or True)
print("False and False", False or False)
print("This is the truth table of and")
# Truth table of 'and' --- if both the value is true it will give true else false (GANDHI)
print("True or False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False", False and False)

# not operator (Jo True ko False aur False ko True bana de usko 'not Operator' kehte hai)

print(not(True)) # not operator is a vice-versa of the value given if not True then it means False
print(not(False)) # if not False it will print True