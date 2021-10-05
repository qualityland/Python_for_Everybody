line = 'X-DSPAM-Confidence:    0.8475 '
ipos = line.find(':')
snum = line[ipos + 1 :].strip()
fnum = float(snum)
print(fnum)
