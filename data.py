#string data type


#literal assignment
first_name='sujithaa'
last_name='raja'

print(type(first_name))
print(type(first_name)==str)
print(isinstance(first_name,str))

#constructor function
name=str("welcome sujithaa")

print(type(name))

full_name=first_name+" "+last_name

print(full_name)
print(type(full_name))
a=13
print(type(a))

#casting a num to str

decade=str(1311)
print(decade)
print(type(decade))

multi_line='''Hello all
welcome suji
good morning                  sujithaa'''
print(multi_line)


sentence='        I\'am Sujithaa \t Welcome \nNew line         '
print(sentence)
print(len(sentence))
print(type(sentence))
print(sentence.lower())
print(sentence.upper())
print(sentence.title())
print(sentence.replace('Welcome','Good Morning'))
print(len(sentence))
sentence=sentence+"new character added         "
print(sentence)
print(len(sentence))

print(len(sentence.strip()))
print(len(sentence.lstrip()))
print(len(sentence.rstrip()))


#MENU
title="menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".")+"$1".rjust(4,"/"))
print("Muffin".ljust(16,".")+"$2".rjust(4))
print("CheeseCake".ljust(16,".")+"$5".rjust(4))

#string index

str='hello'
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])

print(str[:])
print(str[0:1])
print(str[:3])
print(str[:2])
print(str[1:4])
print(str[-1])
print(str[-2])
print(str[::-1])
print(str[::-2])
print(str[::1])
print(str[::2])

print(str.startswith("h"))
print(str.endswith("l"))

#boolean datatype

value=True
ans=bool(False)
print(type(value))
print(type(ans))
print(isinstance(ans,bool))

#integer datatype
price=100
x=int(50)
print(type(price))
print(type(x))
print(isinstance(price,int))

#float datatype
price_ffl=100.90
x_ffl=float(50)
print(type(price_ffl))
print(type(x_ffl))
print(isinstance(price_ffl,float))

#complex value
comp_value=5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built in functions for numbers
y=-20.87
print(abs(y*-1))
print(abs(y*1))
print(round(y))
print(round(y,1))


#using functions from libraries
import math
print(math.pi)
print(math.sqrt(81))
print(math.ceil(y))
print(math.floor(y))

#casting string to numbers

zipcode="639001"
zipvalue=int(zipcode)
print(type(zipvalue))

#error if you attempt to cast incorrect data
#zip_value=int("abc")