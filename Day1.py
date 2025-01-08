'''
sorting dict based on key
'''

d={23:'a',11:'b',2002:'c'}
sorted_key={key:d[key] for key in sorted(d)}
print(sorted_key)

'''
merging 3 dictionary
'''

d1={'a':1,'b':2,'c':3}
d2={'p':4,'q':5,'r':6}
d3={'x':7,'y':8,'z':9}
d=d1.update(d2)
d=d1.update(d3)
print(d1)

'''
find and print the longest line in file 
'''
max_len=0
with open("a.txt","r") as f:
    for line in f:
        words=line.split()
        length=len(words)
        if length>max_len:
            max_len=length
            if len(words)==max_len:
                word=' '.join(words)
                print(word)
    print(max_len)


'''
printing first non-repeating character
'''

s="kkavya"
non_rep=""
for i in s:
    if s.count(i)==1:
        print(i)
        break