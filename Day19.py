'''
adding numbers using decorators
'''

def decorator(func):
    def wrapper1(a,b):
        print("Decorator before")
        if a<b:
            a,b=b,a
        func(a,b)
        print("Decorator afer")
    return wrapper1 
@decorator 
def div(a,b):
    print("Total:",a/b)
div(2,4)


'''
single inheritance
'''

class parent:
    def __init__(self,name):
        self.name=name 
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age 
    def display(self):
        print("Hello this is",self.name,"Age is",self.age)
#p1=parent()
c1=child("Ramya",21)
c1.display()