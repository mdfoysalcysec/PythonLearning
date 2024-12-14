x = 10.3214
print(x)
print(type(x))

y = int(x) # Here we are converting the x float type vriable to int variable and keeping it in y variable
print(y)
print(type(y))



name = 'Foysal' #string
age = 25 #intger
# print('My name is '+ name + '\nMy age is '+ age) #it will not run because name and age are different datatypes
print('My name is '+ name + 'My age is '+ str(age)) # Here we converting the age integer value to a string for just this print only



#There is another method to print two or more different type of variable in a single line
name = 'Foysal' #string
age = 25 #intger
print('My name is {} and My age is {}'.format(name,age))
