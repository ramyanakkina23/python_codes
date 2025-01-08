'''
accepts a filename from the user and prints the extension of the file.
'''
a=input("Enter:")
f=a.split(".")
print(f)
print(f[-1])

'''
accpeting 11,12,2024 as 11/12/2024
'''
date=input("Enter:").split(",")
d1="/".join(date)
print(d1)