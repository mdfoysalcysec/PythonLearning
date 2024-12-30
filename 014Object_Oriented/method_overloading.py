# class calculator:
#     def product(self, num1, num2): #product is a method
#         print(num1 * num2)

#     def product(self, num1, num2, num3): #product is a method
#         print(num1 * num2*num3)


# #Same named method but different parameters mean method overloading
# c1 = calculator() #c1 is an object
# c1.product(10,5) #if we put here 3 again then it will work 
# c1.product(10,5,3)
#--------------------------------------------------------------------------------

class Calculator:
    def values(self, num1, num2=None, num3=None):
        if num1 is not None and num2 is not None and num3 is not None:
            print(num1 * num2 * num3)
        elif num1 is not None and num2 is not None:
            print(num1 * num2)
        else:
            print(num1)

c1 = Calculator()
c1.values(2)
c1.values(2,4)
c1.values(3,3,3)
print('Easier Part starting here')

#------------------------------------------------------------------------------------
#Lets do it easier
#------------------------------------------------------------------------------------

class calculator2:
    def values(self, *nums):
        sum = 1
        for x in nums :
            sum = sum * x
        print(sum) 
s1 = calculator2()
s1.values(100)
s1.values(100,10)