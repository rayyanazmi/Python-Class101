# Q. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your name: ")

if(len(username)<10):
    print("Your username contains less than 10 characters", username)
else:
    print("Your username contains more than 10 characters", username)