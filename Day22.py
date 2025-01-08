'''Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
i/p: 2
o/p: {1:1,2:4}
'''

n=int(input("enter:"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)

'''
write a program to opens a file and handles a FileNotFoundError exception
'''
try:
    with open("h.txt","r") as f:
        content=f.read()
        print(content)
        f.close
except:
    print("File not found")

