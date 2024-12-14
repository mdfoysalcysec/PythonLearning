pylist = [1,3,4,5,6,8,10,9,9,9]
pylist.append(9) #append add value in the last of the list
print(pylist)

#we can copy a variable's full list to another variable
pylist2 = pylist.copy()
print(pylist2)

print(pylist2.count(9)) #Here 9 exist 4 times so the out put will be 4


#we can extend a list with another one
pylist4 = [100, 50, 2, 54, 66]
pylist.extend(pylist4)
print(pylist)