import re
fhand = open('regex_sum_1370897.txt')
numlist = list()
for line in fhand:
    line = line.strip()
    nums = re.findall('([0-9]+)', line)
    if len(nums) < 1 : continue
    for num in nums:
        numlist.append(int(num))
print('sum:', sum(numlist))
