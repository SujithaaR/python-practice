#lists

grocery_list = ['apple','milk','brinjal']
data=['sujithaa',13,True]
emptylist=[]

print('banana' in grocery_list)
print(data[1])
print(data[-1])
print(grocery_list.index('milk'))
print(grocery_list[0:2])
print(grocery_list[:])
print(grocery_list[::-1])
print(grocery_list[-3:-1])

print(len(grocery_list))
print(len(emptylist))

grocery_list.append('banana')
print(grocery_list)

grocery_list+=['rice','orange']
print(grocery_list)

print('')
grocery_list.extend(['fish','chicken'])
print(grocery_list)

print('')
grocery_list.extend(data)
print(grocery_list)

print('')
grocery_list.insert(0,'mutton')
print(grocery_list)

print('')
grocery_list[2:2]=['pepper','onion']
print(grocery_list)

print('')
grocery_list[1:3]=['chilli','tomato']
print(grocery_list)#replace the existing elements

print('')
grocery_list.remove(13)
print(grocery_list)

print('')
grocery_list.remove(True)#remove this element in lists
print(grocery_list)

print('')
print(grocery_list.pop())#remove the last element
print(grocery_list)

print('')
del grocery_list[0]#delete the element with its index value
print(grocery_list)

#del data for deleting the lists

print('')
data.clear()
print(grocery_list)

print('')
print(grocery_list.sort())#sorting the elements in lists
print(grocery_list)

print('')
grocery_list[1:2]=['Salt']
grocery_list.sort()
print(grocery_list)

print('')
grocery_list.sort(key=str.lower)
print(grocery_list)


#number list

num=[1,7,3,4,56,98,23]
num.reverse()
print(num)

num.sort()#ascending,values will be changed in the original list
print(num)

num=[2,45,32,67,83]
print(num)
print(sorted(num,reverse=True))#actual values is not changed in original list
print(num)

#copying list using three ways
#copy method
#list method
#using slicing
numcopy=num.copy()
mynum=list(num)
mycopy=num[:]
print(numcopy)
print(mynum)
print(mycopy)

print(num)
print(type(num))

#using constructor for creating list
mylist=list([1,"suji",False])
print(mylist)