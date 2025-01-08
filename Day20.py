'''
how to replace only the second occurrence of a word/character
output: apple banana kiwi orange apple
'''

def replace_second_occurrence(text, old, new):
    first_index=text.find(old)
    if first_index!=-1:
        sec_index=text.find(old,first_index+len(old))
        if sec_index!=-1:
            return text[:sec_index]+new+text[sec_index+len(old):]
    return text

text = "apple banana apple orange apple"
new_text = replace_second_occurrence(text, "apple", "kiwi")
print(new_text)


'''
Enumerate  function example
'''

#with list
lst=['tarun','ganesh','siva','ajay']
for num,name in enumerate(lst,start=1):
    print(num,name)
#with tuple
tup=('tarun','ganesh','siva','ajay')
for num,name in enumerate(lst,start=0):
    print(num,name)
#with string
text = "hello"
for index, char in enumerate(text):
    print(f"Character at index {index} is '{char}'")
#with list of tuples
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
for i, (name, age) in enumerate(people):
    print(f"{i}: {name} is {age}")
