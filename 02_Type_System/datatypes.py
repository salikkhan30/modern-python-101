

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
phoneList : dict ={'Name' : 'SALIK KHAN', 'PhoneNumber' : '4328u38'}
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


''' 
=========================
Manipulation with Bytes
=========================
'''
# Manipulate bytes
'''
file1 = b"salik khan" # Assgin
for x in file1:         # Loop to print individual byte in ASC 11
    print(x)
file1 = file1[6:10] # Slicing the bytes 
print(file1)
file1 = "New String"    
print(file1)
file1 = file1.encode("utf-8")   # Convert string into bytes
print(file1)
'''

''' 
=========================
Create a phonebook dictionary that sames numbers (unique) with thier names
=========================
'''
# Create Dictionary
'''
phoneList = {'number':'1111', 'name':'John'}
print(phoneList)
phoneList = dict(number='1111', name='Salik')
print(phoneList)
'''
#Access dict
'''
print(phoneList['number'] , phoneList['name'])
print(phoneList.get("name", 0))
print(phoneList["Name"])    # Gives error if not exist
print(phoneList.get("Name1", "customReturnError"))
'''
#Update and Adding new one
'''
phoneList['Name'] = 'John 1'
phoneList['age'] = 32 # Add new column
print(phoneList.get('Name', 'Name-N/A' + str(0)), phoneList.get('PnoneNumber', 'PH-N/A'), phoneList.get('age', 'Age-N/A'))
'''
# Delete Dictionary
'''
del phoneList['name']
print(phoneList)
del phoneList['name']   #gives error if not exist
print(phoneList)

phoneList.pop('name')
print(phoneList)
phoneList.pop('name2') # Gives error if not exist
print(phoneList)
phoneList.clear()
print(phoneList, type(phoneList))
'''

''' 
=========================
Assigning To RANGE DataTypes Variables
=========================
'''
#Assigning 
'''
myRange = range(1,10,2)
print(myRange)
print(myRange[0], myRange[2] , myRange[4])
listing = list(myRange)
print(listing)
'''

''' 
=========================
Assigning To TUPPLE DataTypes Variables
=========================
'''
#Assigning
'''
favhoblist = list(favoriteHobies) # Tuple cannot be changed so convert into another datatype , modify & back to tuple
favhoblist[1] = "changed Hobby"
favoriteHobies = tuple(favhoblist)
print(favoriteHobies[1])
print(favoriteHobies)

favoriteHobies = favoriteHobies[:1] + tuple(favhoblist[1:2]) + favoriteHobies[2:] 
print(favoriteHobies)

'''

''' 
=========================
Assigning To LIST DataTypes Variables
=========================
'''
#Manipulation
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

# Some List Methods
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

