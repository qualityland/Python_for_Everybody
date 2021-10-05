fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File not found:', fname)
    quit()
for line in fhand :
    print(line.rstrip().upper())
