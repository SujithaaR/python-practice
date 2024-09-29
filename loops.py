#while loop

i=1
while i<10:
    i+=2
   
    if i==3:
        #break
        continue
    print(i)
else:
    print("condition failed") 
#-----------------------------------------------------------
#for loop
fruits=["apple","orange","grape"]
for x in fruits:
    if x == "orange":
        #break
        continue
    print(x)  

for x in "Share":
    print(x) 
#--------------------------------------------------------------------
for x in range(10):
    print(x)

for x in range(2,5):
    print(x)

for x in range(0,101,5):#increment of 5
    print(x)
else:
    print("condition finished")
#-----------------------------------------------------------
name=["suji","dfsdf","fsdf"]
actions=["code","sleep","eat"]

for x in name:
    for y in actions:
        print(x+" "+y+".")

for x in actions:
    for y in name:
        print(x+" "+y+".")  
#-------------------------------------------------------------- 