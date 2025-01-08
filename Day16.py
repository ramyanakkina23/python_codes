'''
Count all letters, digits, and special symbols from a given string
'''

str1 = "P@#yn26at^&i5ve"
chars,digits,symbols=0,0,0
for i in str1:
    if i.isalpha():
        chars+=1
    elif i.isdigit():
        digits+=1
    else:
        symbols+=1
print(f"chars = {chars}")
print(f"Digits = {digits}")
print(f"symbols = {symbols}")


"""
#Slice a given list into 3 equal chunks and reverse each chunk
"""

l=[1,2,3,4,5,6,7,8,9]
k=len(l)//3
l1,l2,l3=l[:k],l[k:(2*k)],l[(2*k):]
print(l1[::-1]+l2[::-1]+l3[::-1])
