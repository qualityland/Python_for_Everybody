import re

x = 'My 2 favorite numbers are 19 and 42'

# one or mor numbers
y = re.findall('[0-9]+', x)
print(y)

x = 'From: Using the : character.'

# greedy
y = re.findall('^F.+:', x)
print(y)

# non-greedy
y = re.findall('^F.+?:', x)
print(y)

# non-whitspace surrounding an @
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)

# extract only part of what's matching
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)
