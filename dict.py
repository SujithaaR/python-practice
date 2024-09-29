
#literal assigning of dictionary
car={
  "brand":"tesla",
  "color":"black",
  "model":"model_3",
  "year":2020
}

#using constructor
car2=dict(brand="tesla",model="model_3")

print(car)
print(car2)
print(type(car))
print(len(car))

#accessing the values in dictinonary
print(car['brand'])#passing keys in bracket to get their values
print(car["color"])

#another way
print(car.get("model")) #using get method

#list all keys
print(car.keys())#using keys method to get all keys

#list all values
print(car.values())#using values method to get all values

#list all key value pairs as tuple
print(car.items())#getting all key values as tuple
#getting whole as list,and the key values pairs as tuple
#dict_items([('brand', 'tesla'), ('color', 'black'), ('model', 'model_3'), ('year', 2020)])

#verify a key exists
print("model" in car)
print("price" in car)

#change values
car["brand"]="nio"
 
#adding item
car.update({"price":10000})

print(car)

#remove items
#print(car.pop())#removing the last item and returning the removed items
print(car.pop("year"))#it will return the value which is removed

print(car)

car["EV"]="yes"

print(car)

print(car.popitem())#it will return the tupple which is removed
print(car)

#delete and clear
car["EV"]="yes"
del car["EV"]#it will delete particular
print(car)

#another way
print(car2)
car2.clear()#will remove all the data inside the list
print(car2)

del car2 #delete the dictionary

#copy dictionary

# car2=car 
#it wont create copy, it just create a reference
#copying using copy method
car2=car.copy()
car2["brand"]="tesla"
print("car2 is ",car2)
print("car is ",car)

#using dict() constructor function 
car3=dict(car)
car3["color"]="purple"
print("car3 is ",car3)

#nested dictionary
#keys cannot be duplicated if used it just overite the values alone
member1={
    "name":"plant",
    "instrument":"brand",
    "name":"bala"
}
member2={
    "name":"page",
    "instrument":"model"
}
band={
    "memberOne":member1,
    "memberTwo":member2
}
print(band)
#{'memberOne': {'name': 'plant', 'instrument': 'brand'}, 'memberTwo': {'name': 'page', 'instrument': 'model'}}
print(band["memberOne"]["name"])
#plant

#key cannot duplacate
print(band["memberOne"]["name"])
#bala


