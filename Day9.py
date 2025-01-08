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
convert json to py and py to json
'''
import json
d='{"name":"ramya","age":21}'
x=json.loads(d)
print(x)

y=json.dumps(x)
print(y)