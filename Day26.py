'''
Write a program to find the words and its count to present in below string and explain the logic
St = “Create a stacked bar chart showing the energy consumption breakdown, by source, for the top 5 energy consuming countries.”
'''

st ='Create a stacked bar chart showing the energy consumption breakdown, by source, for the top 5 energy consuming countries.'
ls=st.split()
d={}
for i in ls:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


'''
2. Write a program to find match using regex from below string
St = hkjhujdgkdNX-8Z-13/Ajkjdjgidjkd
match = NX-8Z-13/A
'''
import re
st='hkjhujdgkdNX-8Z-13/Ajkjdjgidjkd'
match=r'^NX-8Z-13/A$'
x=re.search(match,st)
if x:
    print("Matched")
else:
    print("Not matched")