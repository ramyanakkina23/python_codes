'''
reverse a integer number
'''

n=int(input("enter:"))
summ=0
while n>0:
    r=n%10
    summ=(summ*10)+r
    n=n//10
print(summ)

'''
list the values of the dictionary in desc order
'''
d={'a':4,'b':1,'c':10,'d':6}
desc=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
print(desc)

'''
convert the nested list to flatten list by using list comprehension
'''
nested_list = [1, [1, 2], 3, [4, 5]]
x = [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]
print(x)

'''
prints the line numbers where the specific word appears in file
'''
w = input("Enter word: ")
with open("file.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        if w in line:
            print(f"Word '{w}' found on line {line_number}: {line.strip()}")

