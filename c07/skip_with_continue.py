fhand = open('../src/mbox-short.txt', 'r')
for line in fhand :
    # skip lines not starting with From:
    if not line.startswith('From:') :
        continue
    # but print the ones that do
    print(line.rstrip())
