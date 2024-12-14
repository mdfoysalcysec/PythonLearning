a = float(input("Ener the value of a : "))
b = float(input('Enter the value of b : '))
result = a/b


if a > b:
    if result%2==0:
        print('a is greater then b and the resut of a/b is even')
    elif result%2==1:
        print('a is greater then b and the resut of a/b is odd')
    else:
        print('a is greater then b but a/b is less then 1 so its 0')

elif a<b:
    if result%2==0:
        print('b is greater then a and the resut of a/b is even')
    elif result%2==1:
        print('b is greater then b and the resut of a/b is odd')
    else:
        print('b is greater then a but a/b is less then 1 so its 0')
elif a==b:
    if result%2==0:
        print('a and b are equal and the result of a/b is even')
    elif result%2==1:
        print('a and b are equal and the result of a/b is odd')
    else:
        print('a and b are equal but a/b is less then 1 so its 0')
else:
    print('The value is less then zero')




