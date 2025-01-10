'''
write an example program using named tuple
'''

from collections import namedtuple
point=namedtuple("point",['a','b'])
p=point(11,12)
print(p[1])
print(p.a)


'''
write an example program using named deque
'''
from collections import deque
d=deque([1,2,3,4])
d.append(5)
d.appendleft(0)
d.pop()
d.popleft()
print(d)