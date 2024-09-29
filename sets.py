#creating set
#set dont allow duplicates
nums={1,2,3,4}
num2=set((1,2,3,4))

print(num2)
print(nums)
print(type(nums))
print(len(num2))
#{1, 2, 3, 4}
# {1, 2, 3, 4}
# <class 'set'>
# 4

#no duplicates allowed
nums={1,2,2,3}
print(nums)
#{1, 2, 3}

#true is a dupe of 1, false is a dupe of zero
nums={1,True,2,False,3,4,0}
#{1,1,2,0,3,4,0}
print(nums)
#{False, 1, 2, 3, 4}

#check if a values is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or a key

#adding new element
nums.add(8)
print(nums)

#adding elements from one set to another
morenum={5,6,7}
nums.update(morenum)
print(nums)

#can use update with lists,tuple and dictionaries too

#merge two sets to create a new set
one={1,2,3}
two={5,6,7}

mynewset=one.union(two)
print(mynewset)

#keep only the duplicates
one={1,2,3}
two={2,3,4}

one.intersection_update(two)#getting duplicates
print(one)

#keep everything except duplicates
one={1,2,3}
two={2,3,4}
one.symmetric_difference_update(two)
print(one)
