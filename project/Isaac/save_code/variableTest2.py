class Unit:
    def __init__(self, hp):
        self.hp = hp;
    def display(self):
        print(self.hp)

unit = Unit(50)

a = 30

for i in range(30):
    a += 1
    if a % 2 == 0:
        pass
    else:
        print(a)

b = False