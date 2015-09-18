
# Open input.txt and read in all the lines in an array.
inFile = open('input.txt','r')
lines = inFile.readlines()

#for loop.
for x in range(0, len(lines)):
    #get line length.
    lineLength = len(lines[x])

    '''
        sort the lines[x], which gives an array so join together. 
        Exclude the new line element by taking the last lineLength-1 elements.
        Compare to lines[x]
    '''
    if ''.join(sorted(lines[x])[-(lineLength-1):]) == lines[x][:lineLength-1]:
        print (lines[x][:lineLength-1]+ " IN ORDER")
    else:
        print (lines[x][:lineLength-1]+ " NOT IN ORDER")