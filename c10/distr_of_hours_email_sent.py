name = input("Enter file:")
if len(name) < 1:
    name = "../src/mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        count[hour] = count.get(hour, 0) + 1

for k,v in sorted(count.items()):
    print(k, v)
