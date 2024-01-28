

#=============
# DATA TYPES
#=============

'''
STR
NUMERIC int float complex
SEQUENCE : list tuple range
MAPPING : dict
SET : set frozenset
BOOLEAN : bool
BINARY : bytes bytearray memoryview
NONE : NoneType
'''
# DECLARE , INITIALIZATION and ACCESS
from types import NoneType


name = 'Salik'
age : int = 33
salary = 50000
addresses : list = ['address 1' , 'address 2' , 'address 3']
favoriteHobies : tuple = ('swiming', 'outing' , 'programming')
myRange : range = range(3, 6)
phoneList : dict ={'salik' : '0321465', 'Ahmed' : '4328u38'}
More : NoneType = None
IsMale : bool = True
anyOther : set = {'absd', 'werwer', 'gfhghfg'}
file1 : bytes = b"String into Bytes"
file2 : bytearray = bytearray(IsMale)
file3 : memoryview = memoryview(file1)

print(name, age , salary)
print('addresses : ' , addresses , type(addresses))
print('favoriteHobies : ' , favoriteHobies, type(favoriteHobies))
print('myRange : ' , myRange, type(myRange))
print('phoneList : ' , phoneList, type(phoneList))
print('More : ' , More, type(More))
print('IsMale : ' , IsMale, type(IsMale))
print('anyOther : ' , anyOther, type(anyOther))
print('file1 : ' , file1, type(file1))
print('file2 : ' , file2, type(file2))
print('file3 : ' , file3, type(file3))




