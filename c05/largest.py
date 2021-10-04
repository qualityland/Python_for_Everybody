largest = None
for i in [9, 41, 12, 3, 74, 15] :
    if largest is None :
        largest = i
    elif i > largest :
        largest = i
print(largest)
