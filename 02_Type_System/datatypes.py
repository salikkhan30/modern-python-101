

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
print("====================== Declare & Initialize To DataTypes Variables ========================")
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



#Assigning To RANGE DataTypes Variables
'''
myRange = range(1,10,2)
print(myRange)
print(myRange[0], myRange[2] , myRange[4])
listing = list(myRange)
print(listing)

'''
#Assigning To TUPPLE DataTypes Variables
'''
favhoblist = list(favoriteHobies) # Tuple cannot be changed so convert into another datatype , modify & back to tuple
favhoblist[1] = "changed Hobby"
favoriteHobies = tuple(favhoblist)
print(favoriteHobies[1])
print(favoriteHobies)

favoriteHobies = favoriteHobies[:1] + tuple(favhoblist[1:2]) + favoriteHobies[2:] 
print(favoriteHobies)

'''

#Assigning To LIST DataTypes Variables
'''
print("====================== Assigning & Accessing To DataTypes Variables ========================")
salary = 550000.34
print(salary)
addresses.append("address 4")   # Adds to the end of the list
addresses.insert(0, "address 0")
addresses.extend(["address 5", "address 6"])

print('addresses : ' , addresses , type(addresses))
addresses[2] = "address 2.1"
print('addresses : ' , addresses , type(addresses))
addresses.remove(addresses[2])
print('addresses : ' , addresses , type(addresses))
addresses.pop()
print('addresses : ' , addresses , type(addresses))
addresses.pop(0)
print('addresses : ' , addresses , type(addresses))
print(addresses[:1] , addresses[2:])
'''
# favoriteHobies
