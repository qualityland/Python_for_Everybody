text = input('Enter text: ')
words = text.split()

print(words)

d = dict()

for word in words :
    d[word] = d.get(word, 0) + 1

print(d)
