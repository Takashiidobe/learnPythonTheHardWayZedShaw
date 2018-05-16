"""hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1,2,3,4]
this is list declaration
"""

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = [];

#then use the rnage function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #sppend is a function that lists use
    elements.append(i) #similar to array.push()

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")

#other list methods in python
#list.append()
#list.extend() (add a list to another list)
#list.insert() (insert elements to the list)
#list.remove() (remove elements from the list)
#list.index()  (removes the first occurence of index in list)
#list.count() (returns occurences of element in list
#list.pop()  (removes element at given index)
#list.reverse() (reverses a list)
#list.sort() (sorts a list given callback function)
#list.copy() (returns a shallow copy of the list)
#list.clear() (removes all items from the list)
