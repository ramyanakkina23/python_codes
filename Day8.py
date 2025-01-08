'''
Write a Python program to remove duplicates from the dictionary.
'''
d={1: 8, 1: 7, 3: 9, 5: 25, 4: 16}
d1={}
for k,v in d.items():
    if v not in d1.items():
        d1[k]=v
print(d1)


'''
find the missing natural numbers 
'''
l=[1,2,3,5,6]
for i in range(1,len(l)):
    if i not in l:
        print(i)