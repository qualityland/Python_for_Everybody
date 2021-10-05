fhand = open('../src/mbox-short.txt', 'r')
for line in fhand :
    if line.startswith('From:') :
        print(line.rstrip())
