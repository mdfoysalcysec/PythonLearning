print(10+20) # This is printing 30

print('Enter nuber: ')
var = input()
var1 = input()
print(var+var1) # why its printing 1020?
# Cause its taking string input automatically.

#Lets find the solution
print('Enter numbers: ')
var2 = input()
var3 = input()
var2x = int(var2)
var3x = int(var3)
print(var2x+var3x)


#its  little tough to write different print function to show 'Enter your number' like this and for converting string to integer
#Lets make it easier

x = int(input('Enter your numebr1: '))
y= int(input('Enter your number2 : '))
print(x+y)

#we can use float inseasted of int data type
