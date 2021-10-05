data = 'From stefan.schmidt@bluemail.ch Mon Oct  4 09:14:16 2021'
print(data)

at_pos = data.find('@')
print(at_pos)

sp_pos = data.find(' ', at_pos) # 2nd param - start at
print(sp_pos)

host = data[at_pos + 1 : sp_pos]
print(host)

