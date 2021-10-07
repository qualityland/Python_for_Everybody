c = {'a':10, 'c':22, 'b':1}
tmp = list()

# list of tuples with k, v exchanged
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

# sort list of tuples in reverse order
# (by value, since this is now the first variable)
tmp = sorted(tmp, reverse=True)
print(tmp)
