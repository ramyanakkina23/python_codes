'''
swap two numbers without using third variable
here im using xor (^) for swapping
input:10 15
output:15 10
'''

def swapping(a,b):
    a=a^b
    b=b^a
    a=a^b
    return a,b
a,b=map(int,input().split())
print(f"before swapping {a} {b}")
a,b=swapping(a,b)
print(f"after swapping {a} {b}")

'''
How to swap two variables in one line in Python 
input:Hii Hello
outpot:Hello Hii
'''

def swapper(v1,v2):
    v1,v2=v2,v1
    return v1,v2
if __name__=='__main__':
    v1,v2=input().split()
    v1,v2=swapper(v1,v2)
    print(f"{v1} {v2}")