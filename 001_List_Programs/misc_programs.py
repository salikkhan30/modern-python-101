

# Write a Python program to sum all the items in a list.
myList = [6, 4, 1, 2]
sum = 0
for l in myList:
    sum += l
print(sum)
# Write a Python program to multiply all the items in a list.
multiply = 1
for l in myList:
    multiply *= l
print(multiply)
# Write a Python program to get the largest number from a list.
max = myList[0]
for l in myList:
    if l > max:
        max = l
print(max)
# Write a Python program to get the smallest number from a list.
max = myList[0]
for l in myList:
    if l < max:
        max = l
print(max)
'''
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first 
and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
'''
myList = ['abc', 'xyz', 'aba', '1221']
count = 0
for l in myList:
    if len(l) > 1 and l[0] == l[-1]:
        count += 1
print(count)

'''
Write a Python program to remove duplicates from a list.
'''
myList = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
unq_item = []
rem_item = []
if not unq_item:
    print('Empty Unique Item')
for l in myList:
    if l in unq_item:
        rem_item.append(l)
    if l not in unq_item:
        unq_item.append(l)
myList = rem_item
rem_item = []
print(myList, unq_item)






