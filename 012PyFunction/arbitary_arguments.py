# def fun(x): Here you just have only one parameter
#     print(x)
# fun(2, 4, 3,5,7) Here you have many argument so it will show an error



def fun(*x): #Here you add an astric with the parameter so it will count all the unknow argument also
    print(x)
fun(2, 4, 3,5,7)

def name(**name1):
    print('Flowers : ', name1)
name(name1='Red Rose', name2='Golden Rose', name3='White Rose', name4= 'Black Rose')