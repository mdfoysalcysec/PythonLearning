class student:
    def __init__(self, name, id):
        self.name = name        #instance variable which we can't print directly with out the creation of object 
        self.id= id             #instance variable which we can't print directly with out the creation of object 
        print('Created object')

s1 = student('Foysal', 101)
s2 = student('Durjoy', 102)

print(s1.name)
print(s2.name)