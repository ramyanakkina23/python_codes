'''
demonstrate the  Diff between python append and extend ? Explain it with a program!
output:
list1 extended with list2: [1, 2, 5, 4, 6]
list1 appended with list2: [1, 2, 5, [4, 6]]
'''

'''append: Adds a single element to the end of the list
extend: adds each element to the list'''

lst1 = [1, 2, 5]
lst2 = [4, 6]
lst1.extend(lst2)
print(f"List1 extended with List2: {lst1}")

lst1 = [1, 2, 5]
lst2 = [4, 6]
lst1.append(lst2)
print(f"List1 appended with List2: {lst1}")


'''
Write a code for even numbers using list comprehension
output: ['one',2,3.0,'four']
'''
n=int(input('enter max limit: '))
lst=[item for item in range(1,n+1) if item%2==0]
lst=[item for item in range(1,n+1,2)]
print(lst)
