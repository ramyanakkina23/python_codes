'''
validate an Ip address
'''

import re
ip_addr="192.168.250.82"
pattern=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
x=re.match(pattern,ip_addr)
if x:
    print("Matched")
else:
    print("Not matched")


'''
return the no of occurances of each element in list
'''
l=["hii","helo","Good","hii","Good","Morning","helo"]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


'''
check email is vaild or invaild
'''
import re
p=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'
email='ramya123@gmail.com'
x=re.match(p,email)
if x:
    print("Matched")
else:
    print("Not Matched")


'''
Count occurrences of an specific element in a list
'''
l=["hii","helo","Good","hii","Good","Morning","helo"]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


