# split
abc = 'With a   lot of           spaces'
print(abc)
stuff = abc.split()
print(stuff)

for word in stuff :
    print(word)

# separator
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))
