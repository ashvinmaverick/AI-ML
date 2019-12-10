#Python Lists

cars = ['Honda', 'Hyundai', 'Maruti Suzuki', 'Mahendra']
print('This is the list of cars \n', cars)

#Python List Operations

cars.append('Volkswagon') #Appending Elements in the list
print(cars)

len(cars) #Length of a list

print(cars[0]) #Printing Specific Element From THe List

cars.remove('Volkswagon') #Removing Element From List
print(cars)

cars.pop() #List Pop

print(cars[1:3]) #List Slicing

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# element 'e' is searched
index = vowels.index('e')

# index of 'e' is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)

#------------------------------------------------------------------------------------------------


#Sets
a={1,3,43,37}
b={67,34,77,90}
#Printing the Sets
print(a,b)

#Union
a|b

#Intersection
a&b

#Difference
a-b

#Symmetric Difference
a^b

#Comparison Operators
print(a==b) #Operator ==
print(a!=b) #Operator !=
print(a>b) #Operator >
print(a<b) #Operator <
print(a>=b) #Operator >=
print(a<=b) #Operator <=

#Logical Operators
print (a and b) #AND Operator
print (a or b) #OR Operator
print (not(a and b)) #NOT Operator

x=90
y=10
#Arithmetic Operations
print(x+y) #Addtion
print(x-y) #Subtraction
print(x*y) #Multiplication
print(x/y) #Division
print(x%y) #Modulous
print(x**y) #Exponent

#Comparison Operators
print(x==y) #Operator ==
print(x!=y) #Operator !=
print(x>y) #Operator >
print(x<y) #Operator <
print(x>=y) #Operator >=
print(x<=y) #Operator <=

#Assignment Operators
z=x+y
print(z) #Operator =
z+=x
print(z) #Add AND
z-=y
print(z) #Subtract AND
z*=x
print(z) #Multiply AND
z/=y 
print(z) #Divide AND

#Logical Operators
print (x and y) #AND Operator
print (x or y) #OR Operator
print (not(x and y)) #NOT Operator

#..................................................

#tuples

#empty tupple
empty=()
print(empty)

#non empty set
tup='python','anaconda'
print(tup)

#concatenation
tup_1=(0,1,2,3)
print(tup+tup_1)

#nested tupples
tup_2=('btech','HM','law','design')
tup_3=(tup,tup_1,tup_2)
print(tup_3)

#repetition
tup_4=('python',)*4
print(tup_4)

#slicing
tup_5=(0,12,43,54,756,'hello','wolrd')
print(tup_5)
print(tup_5[1:])
print(tup_5[0:4])
print(tup_5[:-1])

#indexing
tup_6 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(tup_6.index(7))
print(tup_6.index(6))



#length
print(len(tup_6))
print(len(tup_5))
print(len(tup_4))
print(len(tup_3))
print(len(tup_2))
print(len(tup))



#conversion list to tupple
list=[0,12,23,34,54]
print(tuple(list))
list_1=['python','java','toc']
print(tuple(list_1))

#adding element
tup_7= (1, 2, 3, 4, 5)
tup_7=tup_7+ (76,)
print(tup_7)

#deleting a tupple
tup_7= (1, 2, 3, 4, 5)
del tup_7


#maximum and minimum
tup_8=(1,32,43,54,65,76)
print(max(tup_8))
print(min(tup_8))
2 in tup_8
54 in tup_8

#------------------------------------------------------------

#Dictionary
Dict = {1: 'BAS', 2: 'ASD', 3: 'ABG'}
print(Dict)
print(Dict.items())#list of tuple pairs
print(len(Dict))#length

#key is present or not
print('A' in Dict) 
print(1 in Dict)

#Nested Dictionary
Dict = {1: 'BAS', 2: 'ASD', 3: {'A' : 'Welcome', 'B' : 'to', 'C' : 'Nested Dict'}}
print(Dict)

#Adding and updating an element
Dict[0] = 'Nj'
Dict[2] = 'Hey'
Dict[3] = 5
print(Dict)

#Accessing using key
Dict = {1: 'First', 'name': 'Name here', 3: '!First'}
print(Dict['name']) 
print(Dict[1]) 

#Accessing using get()
print(Dict.get(3))

#Deletion in DIctionaries

Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Deletion', 
        'A' : {1 : 'One', 2 : 'Two', 3 : 'Three'}, 
        'B' : {1 : 'AOne', 2 : 'BTwo'}} 

  
# Deleting a Key value 
del Dict[6] 
print(Dict) 
  
# Deleting a Key from Nested Dictionary 
del Dict['A'][2] 
print(Dict) 
  
# Deleting a Key using pop() 
Dict.pop(5) 
print(Dict) 
  
# Deleting Key-value pair using popitem() 
Dict.popitem() 
print(Dict) 
  
# Deleting entire Dictionary 
Dict.clear() 
print(Dict) 

#update
Dict = {'A': 18,'C':12,'T':22,'R':25}	
Dict.update({"S":9})
print(Dict)

#Demo Changes
print('Demo Changes')