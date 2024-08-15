name = "rayyan"

print(name[0:3])

print(name[-4: -1]) #Negative
print(name[2:5]) #Positive
print(name[1:]) #blank at start means 0 and blank at end means length of the name
print(name[1:6]) # same as [1:]
print(name[:6]) # same as [0:6] 

word = "amazing" #slicing with skip value
print(word[1:6])
print(word[1:6:2])