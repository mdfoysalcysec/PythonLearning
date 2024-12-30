file = open('cfc.txt', 'w')

if file:
    print('File created successfully')
else:
    print('Failed to create')

#By this I can write something in the file
with open('cfc.txt', 'w') as file1:
    file1.write('Hello, I can write anything from here also. ')

#by this i can read also that what exist in tthe file
with open('cfc.txt', 'r') as file1:
    x = file1.read()
    print(x)


#By this I can write something in the file but everytime I am writing its overwriting
#So we can use append here
with open('cfc.txt', 'a') as file1:
    file1.write('Hi! This is the second test')

#Check the second text has been added
with open('cfc.txt', 'r') as file1:
    x = file1.read()
    print(x)
