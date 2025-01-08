'''
counting no.of letters in a file
'''

d={}
with open("f.txt","r") as f:
    for line in f:
        for word in line:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
print(d)

'''
printing all numbers in a file 
'''

with open("g.txt","r") as f:
    for line in f:
        words=line.split()
        for word in words:
            if word>='0' and word<='9':
                print(word)