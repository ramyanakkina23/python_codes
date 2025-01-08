'''
program to find the largest element without built-in functions
'''
l=[45,78,678,1,0,46,90]
largest1=0
largest2=0
for i in l:
    if i>largest1:
        largest2=largest1
        largest1=i
    if i>largest2 and i!=largest1:
        largest2=i
print(largest2)


'''
program to find the even largest and odd largest element in a list
'''

l=[34,65,78,89,13,54,32,890,6537,97]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",even)
s1=sorted(even)
print(s1[-1])

print("Odd:",odd)
s2=sorted(odd)
print(s2[-1])