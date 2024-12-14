month1 = {'January', 'March', 'May'}
month2 = {'February', 'April', 'June', 'January'}

union = month1.union(month2)
print(union)
intersec = month1.intersection(month2)
print(intersec)

differ = month1.difference(month2)
print(differ)

differ2 = month2.difference(month1)
print(differ2)

symenticdiffer = month1.symmetric_difference(month2)
print(symenticdiffer)