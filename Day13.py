'''
kth smallest element
'''

l=[7, 10, 4, 3, 20, 15]
n=int(input("enter:"))
lst=sorted(l)
print(lst)
print("Kth smallest element:",lst[n-1])

'''
program to find the first non-repeated element in a list.
'''

l=[7, 7, 10, 4, 3, 20, 15]
for i in l:
   if l.count(i)==1:
       print(i)
       break