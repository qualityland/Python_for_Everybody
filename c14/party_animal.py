
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x += 1
        print(self.name,'party count', self.x)

    def __del__(self):
        print(self.name,'destructed', self.x)

s = PartyAnimal('Sally')

# print(type(s))
# print(dir(s))

s.party()
s.party()
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
print('=====',j.name)
s = 1
j.party()

j = 2
