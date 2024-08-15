#  Q. What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s)) # Output will be 2 bcz 20 == 20.0 is same so Sets prints unique value