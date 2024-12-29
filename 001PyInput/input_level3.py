name = input('Enter your full name : ')
age = input('Enter your age : ')

print('Profile Name : {}\nAge: {}'.format(name,age))


#we can do multiple input in single line
5
car_brand, car_model = input('Enter your car brand and model : ').split()

print('Car Brand: {}\nModel: {}'.format(car_brand, car_model))