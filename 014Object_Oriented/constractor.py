#At the method code we saw we had to put value in the value method each time but its pain
#So we will put value direct in the object's parameter

class student:
    roll =''
    cgpa = ''
    def __init__(self,roll,cgpa): #This is tthe constructor here thats why we can add value in the student class's each object directly
        self.roll = roll
        self.cgpa = cgpa

    def info(self):
        print(f'Studet\'s Roll :{self.roll} and his CGPA: {self.cgpa}')
        
Foysal = student(101, 3.35)
Foysal.info()
Durjoy = student(102, 3.50)
Durjoy.info()
Monir = student(103, 3.20)
Monir.info()