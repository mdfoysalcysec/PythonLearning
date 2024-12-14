age = input('Enter your age : ')
if int(age) >= 18:
    def full_name():
        first_name = input('Enter your first name : ')
        last_name = input('Enter your last name: ')
        name= first_name+' '+last_name
        print('Welcome '+ name)
    full_name()

else:
    print('you are not eligible to enter')