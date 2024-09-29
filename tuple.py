mytuple=tuple(('suji',42,True))
anothertuple=(1,2,3,4,5,'food')

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

mylist=list(mytuple)
print(mylist)
mylist.append("neil")
print(mylist)
newtuple=tuple(mylist)

print(newtuple)

#unpackaging tuple

(one,*two,hey)=anothertuple
print(one)
print(two)
print(hey)

#count the no of elements in tuple
print(anothertuple.count(2)) #2 comes only once in the tuple
