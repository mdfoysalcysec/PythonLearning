class student: #here student is the class name
    roll = ''
    cgpa = ''

    #Here this will not be called a function, it is a mthod named info and self is the parameter
    def info(self):
        print(f'Studet\'s Roll :{self.roll} and his CGPA: {self.cgpa}')

    def value(self, roll, cgpa):
        self.roll = roll
        self.cgpa = cgpa

Foysal = student() #Here Foysal is the object under the student class
Foysal.value(101, 3.35)
Foysal.info()

Durjoy = student() #Here Durjoy is the object under the student class
Durjoy.value(102, 3.50)
Durjoy.info()


Monir = student() #Here monir is the object under the student class
Monir.value(103, 3.20)
Monir.info()