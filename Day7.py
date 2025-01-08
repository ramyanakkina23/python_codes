'''
removing the target element
'''

s='hello'
l=list(s)
target=int(input("enter:"))
if target>=0 and target<len(l):
    l.pop(target)
print(l)


'''
taking inputs from command line in dict
'''
n=int(input("enter:"))
d={}
for i in range(n):
    k=input("enter:")
    v=int(input("Enter:"))
    d[k]=v
print(d)