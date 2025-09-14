# varibales 
a = 10 
b = 10 
# a and b are point to the same memory location 
print(id(a))
print(id(a))


#--------------- datatypes ------------------------

#--------------built-in types----------------------

# -----None -------
a = None
print(type(a)) #<class 'NoneType'>

#----Numeric------
# int ( whole number)
b = 1222
print(type(b)) # <class 'int'>

# loat number
c = 22.3
print(type(c)) # <class 'float'>
# complex number
d = 2 + 3j
print(type(d)) # <class 'complex'>

# ----bool -----
# True & False 
print(type(True)) # <class 'bool'>
print(True + True ) # 2 
print(True - False) # 1

# ----- String------
e = "goutam"
print(type(e)) 

# ----- list------
f = [1 , 2 , "str" , True ]
print(type(f)) 

# ----- Touple------
g = (1 , 2 , "str" , True)
print(type(g)) 
# ----- Range------
rg = range(5)
for i in rg:
    print(i)

rgc = range(10 , 20 , 2)
for i in rgc:
    print(i)


# ----- sets-------
data = {10 , 20 , 30 , "goutam" , 40}
print(data)
# ----- Dictionary------

datas = {
    "name" :"goutam" , 
    "email" :"goutamwaghe"
}

print(datas)