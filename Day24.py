'''
give an example program for multi - level inheritance
'''

class grandfather:
    def display1(self):
        print("grandfather")
class father(grandfather):
    def display2(self):
        print("father")
class child(father):
    def display3(self):
        print("child")
c = child()
c.display1()
c.display2()
c.display3()

'''
give an exampe program for default constructor
'''
class person:
    def __init__(self):
        self.name="ramya"
        self.age=21
p=person()
print(p.name)
print(p.age)
