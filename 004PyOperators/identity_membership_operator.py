x = ['Apple', 'Orange', 'Lichi']
y = ['Pinaple', 'Multa', 'Strawberry']

z = x

print(x is y) #Here 'is' is the identity operator
print(x is not z) # It is false cause x is z but we use 'is not' identity operator so its false
print(x is not y) # Cause x is not y


print('Apple' in x) #Here this 'in' is the memebership operator as Apple exist in x so its true