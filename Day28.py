'''
Write a Python script to sort(ascending and descending) a dictionary by value.
'''

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
l = []
for v in d.values():
    l.append(v)
print(l)
print(sorted(l))
l.sort(reverse=True)
print(l)

'''
Write an example program using collections
'''
from collections import deque
d=deque([1,2,3,4])
d.append(5)
d.appendleft(0)
d.pop()
d.popleft()
print(d)