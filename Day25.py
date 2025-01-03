'''
write a program for printing a sentence for n time using decorators
'''

def repeat(run_time):
    def decorator(func):
        def wrapper1(*args,**kwargs):
            print("Printing For required no.of times:")
            for i in range(run_time):
                func(*args,**kwargs)
            print("end....")
        return wrapper1
    return decorator
@repeat(run_time=3)
def fun(name):
    print("Hello",name)
fun("John")


'''
write a program for swapping of 2 num in a list
'''

l=[1,2,3,4]
for i in range(len(l)-1):
    l[i],l[i+1]=l[i+1],l[i]
print(l)