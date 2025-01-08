'''
rename keys of dictonary
'''

d1={1:'one',2:'two'}
d2={}
for key,val in d1.items():
    k=input()
    d2[k]=val
print(d2)


'''
count no of nested keys
'''

d1={1:'one',2:'two'}
d2={3:'three',4:'four',5:'five'}
d3={6:'six'}
d={'d1':d1,'d2':d2,'d3':d3}
print(d)
count=0
for v in d.values():
    for k in v.keys():
        count+=1
print(count)
