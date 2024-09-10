# Q. Write a program which finds out whether a given name is present in a list or not.

a = ["Rayyan", "Harry", "Sumit", "Sid"]

name = input("Enter your name: ")

if(name in a):
    print("Your name is in the list")
else:
    print("Your is not listed")