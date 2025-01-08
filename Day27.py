'''
Count all letters, digits, and special symbols from a given string
input : str1 = "P@#yn26at^&i5ve"
output :
Total counts of chars, digits, and symbols

Chars = 8
Digits = 3
Symbol = 4
'''

s = "P@#yn26at^&i5ve"
chars=0
digits=0
symbols=0
for i in s:
    if i.isalpha():
        chars+=1
    elif i.isdigit():
        digits+=1
    else:
        symbols+=1
print("chars:",chars)
print("Digits:",digits)
print("Symbols:",symbols)


'''
Remove special symbols / punctuation from a string
str1 = "/*I am a @developer & musician"
output = "I am a developer musician"
'''

s="/*I am a @developer & musician"
sp=""
for i in s:
    if i.isalpha() or i.isspace():
        sp+=i
print(sp)