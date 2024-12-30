class student: #here student is the class name
    roll = ''
    cgpa = ''

Foysal = student() #Here Foysal is the object under the student class
Foysal.roll = 101
Foysal.cgpa = 3.35

Durjoy = student() #Here Durjoy is the object under the student class
Durjoy.roll = 102
Durjoy.cgpa = 3.50

Monir = student() #Here monir is the object under the student class
Monir.roll = 103
Monir.cgpa = 3.15

print(f'Foysal\'s Roll :{Foysal.roll} and his CGPA: {Foysal.cgpa}')
print(f'Durjoy\'s Roll :{Durjoy.roll} and his CGPA: {Durjoy.cgpa}')
print(f'Monir\'s Roll :{Monir.roll} and his CGPA: {Monir.cgpa}')