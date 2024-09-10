# Q. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

'''l = ["Rayyan", "Arsalan", "Sumit", "Sid"]'''

l = ["Rayyan", "Arsalan", "Sumit", "Sid"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
