# concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print('c is', c)

# slicing
t = [9, 41, 12, 3, 74, 15]
print('t is',t)
print('t[1:3] is', t[1:3])
print('t[:4] is', t[:4])
print('t[3:] is', t[3:])
print('t[:] is', t[:])

# methods
x = list()
print(type(x))
print(dir(x))

# constructor
stuff = list()

# append
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# in
some = [1, 9, 21, 10, 16]
print(9 in some)        # True
print(15 in some)       # False
print(20 not in some)   # True

# sort
# lists keep their order, but can be sorted
friends = ['Joseph', 'Glenn', 'Sally']
print('original:', friends)
friends.sort()
print('sorted:', friends)

nums = [3, 41, 12, 9, 74, 15]

# length
print('len:', len(nums))

# maximum
print('max:', max(nums))

# minimum
print('min', min(nums))

# sum
print('sum', sum(nums))

# average (sum / len)
print('sum/len:', sum(nums)/len(nums))
