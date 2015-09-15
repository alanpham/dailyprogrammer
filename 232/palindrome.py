# Opened the input.txt.
f = open('input.txt', 'r')
s = int(f.readline())

inputstr = ""

# Reads in the input and puts it into inputstr
for x in range(0, s):
    inputstr += f.readline()

# Joins 
w = ' '.join(c for c in inputstr.lower() if c.isalpha())

if w == w[::-1]:
    print("Is Palindrome")
else:
    print("Is not a Palindrome")