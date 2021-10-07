d = {'a':10, 'c':22, 'b':1}
print(d)
t = sorted(d.items())
print(t)

for k, v in sorted(d.items()):
    print(k, v)
