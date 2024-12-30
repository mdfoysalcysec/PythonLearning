# class student:

#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
        
#     def __init__(self,name,id, cgpa):
#         self.name = name
#         self.id = id
#         self.cgpa = cgpa

# s1 = student('Foysal', 101)
# s2 = student('Durjoy', 102, 3.50)
#This will not work cause we don't pass the third parameter
#========================================================================#

#Let's make it working
class student:
    def __init__(self, *info):
        if len(info) == 3:
            self.name = info[0]
            self.id = info[1]
            self.cgpa = info[2]
        elif len(info) == 2:  # Handle case with two arguments
            self.name = info[0]
            self.id = info[1]
            self.cgpa = None  # Optional if CGPA isn't provided
        elif len(info) == 1:  # Handle case with one argument
            self.name = info[0]
            self.id = None
            self.cgpa = None

    def __str__(self):
        # Define how to display the student object
        return f"Name: {self.name}, ID: {self.id}, CGPA: {self.cgpa}"


s1 = student('Foysal', 101)
s2 = student('Durjoy', 102, 3.50)

# Print the details of s1
print(s1)