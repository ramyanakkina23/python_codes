'''
swaps the keys with values in a dictonary
'''
d={'a':1,'b':2,'c':3}
d1={}
for k,v in d.items():
    k,v=v,k
    d1[k]=v
print(d1)

'''
Find Common Characters in Two Strings
'''
s1="hihello"
s2="hellogoodmorning"
for i in s1:
    if i in s2:
        print(i,end=" ")