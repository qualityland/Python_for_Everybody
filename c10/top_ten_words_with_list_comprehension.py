fhand = open('../src/romeo-full.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# lst = list()
# for k, v in counts.items():
#     lst.append((v, k))
#
# lst = sorted(lst, reverse=True)

# list comprehension
lst = sorted([(v,k) for k,v in counts.items()], reverse=True)

for v, k in lst[:10]:
    print(k, v)
