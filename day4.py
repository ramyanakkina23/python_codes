'''
Anagrams
'''
s1=input("enter s1:")
s2=input("enter s2:")
if len(s1)==len(s2) and sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")

'''
remove duplicates from a string
'''
s="hii hello good hii good hello morning how are you"
l=s.split()
se=set(l)
print(se)

'''
return the statement where each word should be starts with capital letter
'''
with open("file.txt","r") as f:
    for line in f:
        words=line.split()
        s=""
        for word in words:
            x=word.title()
            s+=x+" "
        print(s)

'''
return the list of words which starts with capital letter only out of statement
'''
with open("file.txt", "r") as f:
    capital_words = []
    for line in f:
        words = line.split()
        capital_words.extend(word for word in words if word[0].isupper())
print(capital_words)

