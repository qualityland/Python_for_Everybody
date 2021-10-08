import re

hand = open('../src/mbox-short.txt')

for line in hand:
    line = line.rstrip()

    # simple search
    # if line.find('From:') >=0:
    if re.search('From:', line):
        #print(line)
        pass

    #if line.startswith('From:'):
    if re.search('^From:', line):
        #print(line)
        pass

    # \S non-whitespace characters
    if re.search('^X-\S+:', line):
        print(line)
