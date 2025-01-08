'''
add ing at end of string.
'''

s=input("Enter:")
if s[-3:]=="ing":
    print("Unchanged str:",s)
else:
    print("Modified str:",s+"ing")

'''
Delete a list of keys from a dictionary
'''

sample_dict = {"name": "ramya","age": 22,"salary": 8000,"city": "Vsp"}
keys = ["name", "salary"]
for key in keys:
    if key in sample_dict.keys():
        sample_dict.pop(key)
print(sample_dict)
