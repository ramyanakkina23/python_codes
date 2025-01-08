'''
program to calculate the difference between a given number and 17 If the number is greater than 17, return twice the absolute difference.
'''
n=int(input("Enter:"))
if n<=17:
    print("diff:",17-n)
else:
    print("Abs diff:",abs((17-n)*2))

'''
program to test whether a number is within 100 of 1000 or 2000
'''

n=int(input("Enter:"))
if abs(1000-n)<=100 or abs(2000-n)<=10:
    print("Near to 1000")
else:
    print("False")