counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

# old-fashioned
for name in names :
    if name not in counts :
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

# get
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)


# keys, values, items
d = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(d)
print(d.keys())
print(d.values())
print(d.items())

for k,v in d.items() :
    print(k, v)
