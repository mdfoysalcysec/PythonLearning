#Two type of constructor number1: default, number2: parameterised...when we are sing self its default when we are passing argument its parameterised

class student:
    def display(self):
        print('This is is a method')

    def __init__(self,x,y):
        print('This is a constructor, Notice one thing carefull constructr is printing before the method, cause costructor priority is more then method')
        print(x,y)

s1 = student(10, 20)
s1.display()