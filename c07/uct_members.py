fhand = open('../src/mbox-short.txt', 'r')
for line in fhand :
    # skip lines not including @uct.ac.za
    if not '@uct.ac.za' in line :
        continue
    # print uct lines
    print(line.rstrip())
