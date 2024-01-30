

#=============
# STRINGS MANIPULATION
#=============

# String are Arrays
'''
name = 'Salik khan'
print(name, name[1] , name[2] , 'Length: ' + str(len(name)), len(name[1]))
'''

# search in string
'''
print('kh' in name)
print('ph' not in name)
'''


# Slicing
'''
print(name)
print(name[:9], name[1:], name[1:5])
print(name[-5:] , name[:-4] , name[-9:-2])
'''

# Upper , lower , Strip
'''
name = '    ' + name + '   '
print(name.upper(), name.lower(), name.strip())
print(len(name), len(name.strip()))
'''

# Replacing string
'''
name = name.replace(' ', '')
print(name)
'''

# String Split
'''
name = ' ,, Salik , khan , '
name = name.split(',')  # On Split converts into list
print(name)
'''


# String Formatting
name = ' SALIK KHAN {} , {}'
print(name.format(30, 20))

name = ' SALIK KHAN {0} , {1}'  # {} starts with zero at any position of string
print(name.format(30, 20))
#print(name + 33) # gives error








