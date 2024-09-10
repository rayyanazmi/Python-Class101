#  Q. Write a program to find out whether a given post is talking about “Rayyan” or not.

post = input("Enter the post: ")

if("Rayyan".lower() in post.lower()):
    print("This post is talking about rayyan")
else:
    print("This post is not talking about rayyan")