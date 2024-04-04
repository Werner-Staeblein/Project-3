# Your code goes here.

# the extra line was added with \n

a = input("Please provide your name with maximum of 10 characters:\n")

if len(a) > 10:
    print("Name is too long")
else:
    print("Name within limits of characters")

