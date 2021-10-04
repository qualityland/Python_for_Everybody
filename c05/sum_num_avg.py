num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    else:
        try:
            fval = float(sval)
        except:
            print('bad data')
            continue
        num += 1
        tot += fval
print(tot, num, tot / num)
