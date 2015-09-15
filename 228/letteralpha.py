# Open input.txt for read only.
inFile = open('input.txt','r')
line = inFile.readline()
if (''.join(sorted(line)) == line):
    print "YES"
#print(if (''.join(sorted(line)) == line))