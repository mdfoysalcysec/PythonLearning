s = {'C', 'Python', 'Java'}
print(s)
s.add('Cython') #When we want to add multiplesingle element
print(s)
print(s)

s1 = {'Kotlin', 'C++', 'C#'}
s.update(s1) #When we want to add multiple element
print(s)

s.discard('Kotlin') #When we want to remove single element
print(s)

s.remove('C#')#When we want to remove single element
print(s)

s.pop() #It will remove the last element
print(s)

us = s.copy() #s copy in us
print(us)

us.clear() # There are vno elements in  the us variable now
print(us)