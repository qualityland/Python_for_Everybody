fruit = 'banana'


# while
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

# for loop
for letter in fruit:
    print(letter)

# counting
count = 0
for i in fruit:
    if i == 'a':
        count += 1
print('count', count)

# slicing
s = 'Monty Python'
print('s[:]', s[:])
print('s[:4]', s[:4])
print('s[6:]', s[6:])
print('s[6:7]', s[6:7])
print('s[6:20]', s[6:20])

# in
print("is 'n' in fruit?", 'n' in fruit)
print("is 'm' in fruit?", 'm' in fruit)
print("is 'nan' in fruit?", 'nan' in fruit)

# class and methods
stuff = 'hello world'
print(type(stuff))
print(dir(stuff))

# find
fruit = 'banana'
pos = fruit.find('na')
print('position of \'na\' is:', pos)

aa = fruit.find('z')
print('position of \'z\' is:', aa)
