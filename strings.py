# Strings
"""
-->Collection of charatcter is called string

--->Group of chararcters is called a string

-->in python string representation is '' or "" or """"""

---> In python string immutable

---> in python string is indexed value based

--->string supports slicing operator--->':'
"""
#a=''' '''
#print(type(a))
'''
a="welcome to python"
print(a)

# concatination of string
b='workshop'
c=a+b
print(c) # a+= 'hello'

# getting values

print(a[0])
print(a[1])

# forwardindex and backword index

# forwardindex

print(a[0])
print(a[5])

# backword index
s="welcome to python"
print(s[-1])
print(s[-5])


# slicing operation-->:

name='python programming'

#print(name[:])
#print(name[0:6])
#print(name[4:6])
#print(name[::-1])
#print(name[0:17:2])
#print(name[6:7])
print(name[0:])
'''
# String Methods 3 ways
# by using datatype--->str
#print(dir(str))
#n=''
#print(dir(n))

#m='hello'
#print(dir(m))

p='  welcome to apssdc  '
#print(p.capitalize())

#print(p.casefold())
#print(p.swapcase())
#print(p.count('S'))
#print(p.index('z'))
#print(p.find('x'))
#print(p.center(20,'*'))
#print('My name is {0} & i am from {1}'.format('abc','xyz'))
#print(p.upper())
#print(p.lower())
#print(p.title())
#print(p.isupper())
#print(p.islower())
#print(p.startswith('w'))
#print(p.endswith('c'))
#print(p.istitle())
q='<--'
#print(q.join(p))
#print(p.isdigit())
#print(p.isalpha())
#print(p.isalnum())
#print('python\tprogtamming\tworkshop'.expandtabs())
'''split,
spltlines,
strip,
lstrip,
rstrip'''

#print(p.split())
#print(p.strip())

print(p.lstrip())
print(p.rstrip())









