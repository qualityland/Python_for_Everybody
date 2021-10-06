fname = input('Enter file: ')

if len(fname) < 1 : fname = '../src/mbox-short.txt'
fhand = open(fname)

# create dictionary of (email, count) items
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

# identify most frequent mailer
bigmail = None
bigcount = None

for mail, count in counts.items():
    if bigcount is None or bigcount < count:
        bigcount = count
        bigmail = mail

print(bigmail, bigcount)
